from datetime import datetime, timedelta, timezone
from owrx.config import Config
from owrx.bands import Band
from abc import abstractmethod, ABC, ABCMeta
import threading
import time
import sys

import logging

logger = logging.getLogger(__name__)


class Location(object):
    def getTTL(self) -> timedelta:
        pm = Config.get()
        return timedelta(seconds=pm["map_position_retention_time"])

    def __dict__(self):
        return {
            "ttl": self.getTTL().total_seconds() * 1000
        }


class Map(object):
    sharedInstance = None
    creationLock = threading.Lock()

    @staticmethod
    def getSharedInstance():
        with Map.creationLock:
            if Map.sharedInstance is None:
                Map.sharedInstance = Map()
        return Map.sharedInstance

    def __init__(self):
        self.clients = []
        self.positions = {}
        self.positionsLock = threading.Lock()

        def removeLoop():
            loops = 0
            while True:
                try:
                    self.removeOldPositions()
                except Exception:
                    logger.exception("error while removing old map positions")
                loops += 1
                # rebuild the positions dictionary every once in a while, it consumes lots of memory otherwise
                if loops == 60:
                    try:
                        self.rebuildPositions()
                    except Exception:
                        logger.exception("error while rebuilding positions")
                    loops = 0
                time.sleep(60)

        threading.Thread(target=removeLoop, daemon=True, name="map_removeloop").start()
        super().__init__()

    def broadcast(self, update):
        for c in self.clients:
            c.write_update(update)

    def addClient(self, client):
        self.clients.append(client)
        with self.positionsLock:
            positions = [
                {
                    "callsign": callsign,
                    "location": record["location"].__dict__(),
                    "lastseen": record["updated"].timestamp() * 1000,
                    "mode": record["mode"],
                    "band": record["band"].getName() if record["band"] is not None else None,
                    "hops": record["hops"],
                }
                for (callsign, record) in self.positions.items()
            ]
        client.write_update(positions)

    def removeClient(self, client):
        try:
            self.clients.remove(client)
        except ValueError:
            pass

    def updateLocation(self, key, loc: Location, mode: str, band: Band = None, hops: list[str] = [], timestamp: datetime = None):
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)
        else:
            # if we get an external timestamp, make sure it's not already expired
            if datetime.now(timezone.utc) - loc.getTTL() > timestamp:
                return

        pm = Config.get()
        ignoreIndirect = pm["map_ignore_indirect_reports"]
        preferRecent = pm["map_prefer_recent_reports"]
        needBroadcast = False

        with self.positionsLock:
            # ignore indirect reports if ignoreIndirect set
            if not ignoreIndirect or len(hops)==0:
                # prefer messages with shorter hop count unless preferRecent set
                if preferRecent or key not in self.positions or len(hops) <= len(self.positions[key]["hops"]):
                    if isinstance(loc, IncrementalUpdate) and key in self.positions:
                        loc.update(self.positions[key]["location"])
                    self.positions[key] = {"location": loc, "updated": timestamp, "mode": mode, "band": band, "hops": hops }
                    needBroadcast = True

        if needBroadcast:
            self.broadcast(
                [
                    {
                        "callsign": key,
                        "location": loc.__dict__(),
                        "lastseen": timestamp.timestamp() * 1000,
                        "mode": mode,
                        "band": band.getName() if band is not None else None,
                        "hops": hops,
                    }
                ]
            )

    def touchLocation(self, key):
        # not implemented on the client side yet, so do not use!
        ts = datetime.now(timezone.utc)
        with self.positionsLock:
            if key in self.positions:
                self.positions[key]["updated"] = ts
        self.broadcast([{"callsign": key, "lastseen": ts.timestamp() * 1000}])

    def removeLocation(self, key):
        with self.positionsLock:
            if key in self.positions:
                del self.positions[key]
                # TODO broadcast removal to clients

    def removeOldPositions(self):
        now = datetime.now(timezone.utc)

        with self.positionsLock:
            to_be_removed = [
                key for (key, pos) in self.positions.items() if now - pos["location"].getTTL() > pos["updated"]
            ]
        for key in to_be_removed:
            self.removeLocation(key)

    def rebuildPositions(self):
        logger.debug("rebuilding map storage; size before: %i", sys.getsizeof(self.positions))
        with self.positionsLock:
            p = {key: value for key, value in self.positions.items()}
            self.positions = p
        logger.debug("rebuild complete; size after: %i", sys.getsizeof(self.positions))


class LatLngLocation(Location):
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __dict__(self):
        res = super().__dict__()
        res.update(
            {"type": "latlon", "lat": self.lat, "lon": self.lon}
        )
        return res


class LocatorLocation(Location):
    def __init__(self, locator: str):
        self.locator = locator

    def __dict__(self):
        res = super().__dict__()
        res.update(
            {"type": "locator", "locator": self.locator}
        )
        return res


class IncrementalUpdate(Location, metaclass=ABCMeta):
    @abstractmethod
    def update(self, previousLocation: Location):
        pass

