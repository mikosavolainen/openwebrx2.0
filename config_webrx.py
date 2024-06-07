# -*- coding: utf-8 -*-

"""
config_webrx: configuration options for OpenWebRX

    This file is part of OpenWebRX,
    an open-source SDR receiver software with a web UI.
    Copyright (c) 2013-2015 by Andras Retzler <randras@sdr.hu>
    Copyright (c) 2019-2021 by Jakob Ketterl <dd5jfk@darc.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    In addition, as a special exception, the copyright holders
    state that config_rtl.py and config_webrx.py are not part of the
    Corresponding Source defined in GNU AGPL version 3 section 1.

    (It means that you do not have to redistribute config_rtl.py and
    config_webrx.py if you make any changes to these two configuration files,
    and use them for running your web service with OpenWebRX.)
"""

"""
DEPRECATION notice

As of OpenWebRX 0.21, the configuration system has been completely overhauled.
The configuration of OpenWebRX should now be done in the new web-based
configuration interface exclusively.

Existing configurations can still be used, but their values will be migrated
to the new storage infrastructure as soon as the web configuration is used to
edit them.

The new configuration storage is not intended to be edited manually.
"""

# configuration version. please only modify if you're able to perform the associated migration steps.
version = 7

# NOTE: you can find additional information about configuring OpenWebRX in the Wiki:
# https://github.com/jketterl/openwebrx/wiki/Configuration-guide

# ==== Server settings ====
#max_clients = 20

# ==== Web GUI configuration ====
#receiver_name = "[OH3CYT]"
#receiver_location = "Lahti, Renkom\u00e4ki"
#receiver_asl = 65
#receiver_admin = "miksa.server@gmail.com"
#receiver_gps = {"lat": 60.993736, "lon": 25.656983}
#photo_title = "OH3CYT SDR"
# photo_desc allows you to put pretty much any HTML you like into the receiver description.
# The lines below should give you some examples of what's possible.
#photo_desc = """
#You can add your own background photo and receiver information.<br />
#Receiver is operated by: <a href="mailto:miksa.server@gmail.com" target="_blank">Receiver Operator</a><br/>
#Device: RTL-SDR v3<br />
#Antenna: Longwire <br />
#Website: <a href="https://oh3cyt.com" target="_blank">https://oh3cyt.com</a>
#"""

# ==== Public receiver listings ====
# You can publish your receiver on online receiver directories, like https://www.receiverbook.de
# You will receive a receiver key from the directory that will authenticate you as the operator of this receiver.
# Please note that you not share your receiver keys publicly since anyone that obtains your receiver key can take over
# your public listing.
# Your receiver keys should be placed into this array:
#receiver_keys = []
# If you list your receiver on multiple sites, you can place all your keys into the array above, or you can append
# keys to the arraylike this:
# receiver_keys += ["my-receiver-key"]

# If you're not sure, simply copy & paste the code you received from your listing site below this line:

# ==== DSP/RX settings ====
#fft_fps = 9
#fft_size = 49152  # Should be power of 2
#fft_voverlap_factor = (
#    0.3  # If fft_voverlap_factor is above 0, multiple FFTs will be used for creating a line on the diagram.
#)

#audio_compression = "adpcm"  # valid values: "adpcm", "none"
#fft_compression = "adpcm"  # valid values: "adpcm", "none"

# Tau setting for WFM (broadcast FM) deemphasis\
# Quote from wikipedia https://en.wikipedia.org/wiki/FM_broadcasting#Pre-emphasis_and_de-emphasis
# "In most of the world a 50 µs time constant is used. In the Americas and South Korea, 75 µs is used"
# Enable one of the following lines, depending on your location:
# wfm_deemphasis_tau = 75e-6  # for US and South Korea
#wfm_deemphasis_tau = 50e-6  # for the rest of the world

#digimodes_fft_size = 2048

# enables lookup of DMR ids using the radioid api
#digital_voice_dmr_id_lookup = True

"""
Note: if you experience audio underruns while CPU usage is 100%, you can:
- decrease `samp_rate`,
- set `fft_voverlap_factor` to 0,
- decrease `fft_fps` and `fft_size`,
- limit the number of users by decreasing `max_clients`.
"""

# ==== I/Q sources ====
# (Uncomment the appropriate by removing # characters at the beginning of the corresponding lines.)

###############################################################################
# Is my SDR hardware supported?                                               #
# Check here: https://github.com/jketterl/openwebrx/wiki/Supported-Hardware   #
###############################################################################

# Currently supported types of sdr receivers:
# "rtl_sdr", "rtl_sdr_soapy", "sdrplay", "hackrf", "airspy", "airspyhf", "fifi_sdr",
# "perseussdr", "lime_sdr", "pluto_sdr", "soapy_remote", "hpsdr", "uhd",
# "radioberry", "fcdpp", "rtl_tcp", "sddc", "runds"

# For more details on specific types, please checkout the wiki:
# https://github.com/jketterl/openwebrx/wiki/Supported-Hardware#sdr-devices

#sdrs = {
# "rtl_sdr_hf": {
#     "name": "RTL-SDR v3 HF USB Stick",
#     "type": "rtl_tcp",
#     "ppm": 0,
#     "direct_sampling": 2,
#     "remote": "192.168.1.123:1234",
#     "profiles": {
#         "10mHAM": {
#             "name": "10mHAM",
#             "center_freq": 28500000,
#             "rf_gain": 25.0,
#             "samp_rate": 2048000,
#             "start_freq": 28000000,
#             "start_mod": "usb",
#             "tuning_step": 1,
#             "direct_sampling": 0,
#             "waterfall_levels": {
#                 "min": -81.0,
#                 "max": -31.0
#             }
#         },
#         "13m": {
#             "name": "12mHAM",
#             "center_freq": 24900000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 24151000,
#             "start_mod": "usb",
#             "tuning_step": 1,
#             "waterfall_levels": {
#                 "min": -86.0,
#                 "max": -36.0
#             },
#             "direct_sampling": 0
#         },
#         "15mHAM": {
#             "name": "15mHAM",
#             "center_freq": 21100000,
#             "rf_gain": 10,
#             "samp_rate": 2048000,
#             "start_freq": 21000000,
#             "start_mod": "usb",
#             "waterfall_levels": {
#                 "min": -86.0,
#                 "max": -27.0
#             },
#             "tuning_step": 1
#         },
#         "16m": {
#             "name": "17mHAM",
#             "center_freq": 18111000,
#             "rf_gain": 10,
#             "samp_rate": 1000000,
#             "start_freq": 18150000,
#             "start_mod": "usb",
#             "tuning_step": 1,
#             "waterfall_levels": {
#                 "min": -86.0,
#                 "max": -16.0
#             }
#         },
#         "20m": {
#             "name": "20mHAM",
#             "center_freq": 14100000,
#             "rf_gain": 10,
#             "samp_rate": 2048000,
#             "start_freq": 14000000,
#             "start_mod": "usb",
#             "tuning_step": 1,
#             "waterfall_levels": {
#                 "min": -87.0,
#                 "max": -15.0
#             }
#         },
#         "30m": {
#             "name": "30mHAM",
#             "center_freq": 10125000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 10142000,
#             "start_mod": "lsb",
#             "waterfall_levels": {
#                 "min": -87.0,
#                 "max": -14.0
#             },
#             "tuning_step": 1
#         },
#         "40m": {
#             "name": "40mHAM",
#             "center_freq": 7100000,
#             "rf_gain": 10,
#             "samp_rate": 2400000,
#             "start_freq": 7050000,
#             "start_mod": "lsb",
#             "waterfall_levels": {
#                 "min": -85.0,
#                 "max": -27.0
#             },
#             "tuning_step": 1
#         },
#         "80m": {
#             "name": "80mHAM",
#             "center_freq": 3700000,
#             "rf_gain": 10,
#             "samp_rate": 1400000,
#             "start_freq": 3699000,
#             "start_mod": "lsb",
#             "tuning_step": 1,
#             "waterfall_levels": {
#                 "min": -88.0,
#                 "max": -32.0
#             }
#         },
#         "11m": {
#             "name": "11m",
#             "center_freq": 26670000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 25670000,
#             "start_mod": "am",
#             "tuning_step": 1,
#             "direct_sampling": 0
#         },
#         "15m": {
#             "name": "15m",
#             "center_freq": 19200000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 18200000,
#             "start_mod": "am"
#         },
#         "19m": {
#             "name": "19m",
#             "center_freq": 16100000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 15100000,
#             "start_mod": "am"
#         },
#         "22m": {
#             "name": "22m",
#             "center_freq": 14570000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 13570000,
#             "start_mod": "am"
#         },
#         "25m": {
#             "name": "25m",
#             "center_freq": 12000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 11000000,
#             "start_mod": "am"
#         },
#         "31m": {
#             "name": "31m",
#             "center_freq": 10000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 9000000,
#             "start_mod": "am"
#         },
#         "41m": {
#             "name": "41m",
#             "center_freq": 8000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 7100000,
#             "start_mod": "am"
#         },
#         "49m": {
#             "name": "49m",
#             "center_freq": 6800000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 5800000,
#             "start_mod": "am"
#         },
#         "60m": {
#             "name": "60m",
#             "center_freq": 5000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 4000000,
#             "start_mod": "am"
#         },
#         "75m": {
#             "name": "75m",
#             "center_freq": 4000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 4625000,
#             "start_mod": "usb",
#             "tuning_step": 1
#         },
#         "90m": {
#             "name": "90m",
#             "center_freq": 4000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 3100000,
#             "start_mod": "am"
#         },
#         "120m": {
#             "name": "120m",
#             "center_freq": 3000000,
#             "rf_gain": 10,
#             "samp_rate": 2000000,
#             "start_freq": 2300000,
#             "start_mod": "am"
#         },
#         "12beaf1b-b4f1-4391-992c-c20717db41e0": {
#             "name": "2m",
#             "center_freq": 144500000,
#             "samp_rate": 2048000,
#             "start_freq": 144,
#             "start_mod": "nfm",
#             "tuning_step": 1,
#             "direct_sampling": 0
#         },
#         "9c07149a-1f70-4cb3-a7c2-57a548531bc8": {
#             "name": "6mHAM",
#             "center_freq": 50100000,
#             "samp_rate": 2048000,
#             "start_freq": 50100000,
#             "start_mod": "usb",
#             "tuning_step": 1,
#             "direct_sampling": 0
#         }
#     },
#     "waterfall_levels": {
#         "min": -77.0,
#         "max": -27.0
#     }
# },
#    "airspy": {
#        "name": "Airspy HF+",
#        "type": "airspyhf",
#        "ppm": 0,
#        "rf_gain": "auto",
#        "profiles": {
#            "20m": {
#                "name": "20m",
#                "center_freq": 14150000,
#                "samp_rate": 384000,
#                "start_freq": 14070000,
#                "start_mod": "usb",
#            },
#            "30m": {
#                "name": "30m",
#                "center_freq": 10125000,
#                "samp_rate": 192000,
#                "start_freq": 10142000,
#                "start_mod": "usb",
#            },
#            "40m": {
#                "name": "40m",
#                "center_freq": 7100000,
#                "samp_rate": 256000,
#                "start_freq": 7070000,
#                "start_mod": "lsb",
#            },
#            "80m": {
#                "name": "80m",
#                "center_freq": 3650000,
#                "samp_rate": 384000,
#                "start_freq": 3570000,
#                "start_mod": "lsb",
#            },
#            "49m": {
#                "name": "49m Broadcast",
#                "center_freq": 6050000,
#                "samp_rate": 384000,
#                "start_freq": 6070000,
#                "start_mod": "am",
#            },
#        },
#    },
#    "sdrplay": {
#        "name": "SDRPlay RSP2",
#        "type": "sdrplay",
#        "ppm": 0,
#        "antenna": "Antenna A",
#        "profiles": {
#            "20m": {
#                "name": "20m",
#                "center_freq": 14150000,
#                "rf_gain": 0,
#                "samp_rate": 500000,
#                "start_freq": 14070000,
#                "start_mod": "usb",
#            },
#            "30m": {
#                "name": "30m",
#                "center_freq": 10125000,
#                "rf_gain": 0,
#                "samp_rate": 250000,
#                "start_freq": 10142000,
#                "start_mod": "usb",
#            },
#            "40m": {
#                "name": "40m",
#                "center_freq": 7100000,
#                "rf_gain": 0,
#                "samp_rate": 500000,
#                "start_freq": 7070000,
#                "start_mod": "lsb",
#            },
#            "80m": {
#                "name": "80m",
#                "center_freq": 3650000,
#                "rf_gain": 0,
#                "samp_rate": 500000,
#                "start_freq": 3570000,
#                "start_mod": "lsb",
#            },
#            "49m": {
#                "name": "49m Broadcast",
#                "center_freq": 6000000,
#                "rf_gain": 0,
#                "samp_rate": 500000,
#                "start_freq": 6070000,
#                "start_mod": "am",
#            },
#        },
#    },
#}

# ==== Color themes ====

### google turbo colormap (see: https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html)
#waterfall_scheme = "GoogleTurboWaterfall"

### original theme by teejez:
#waterfall_scheme = "TeejeezWaterfall"

### old theme by HA7ILM:
#waterfall_scheme = "Ha7ilmWaterfall"
##For the old colors, you might also want to set [fft_voverlap_factor] to 0.

### custom waterfall schemes can be configured like this:
#waterfall_scheme = "CustomWaterfall"
#waterfall_colors = [0x0000FF, 0x00FF00, 0xFF0000]

### Waterfall calibration
#waterfall_levels = {"min": -88, "max": -20}  # in dB

#waterfall_auto_levels = {"min": 3, "max": 10}
#waterfall_auto_min_range = 50

# Note: When the auto waterfall level button is clicked, the following happens:
#   [waterfall_levels.min] = [current_min_power_level] - [waterfall_auto_levels["min"]]
#   [waterfall_levels.max] = [current_max_power_level] + [waterfall_auto_levels["max"]]
#
#   ___|__________________________________|____________________________________|__________________________________|___> signal power
#        \_waterfall_auto_levels["min"]_/ |__ current_min_power_level          | \_waterfall_auto_levels["max"]_/
#                                                    current_max_power_level __|

# This setting allows you to modify the precision of the frequency displays in OpenWebRX.
# Set this to exponent of 10 to select the most precise digit in Hz you'd like to see
# examples:
# a value of 2 selects 10^2 = 100Hz tuning precision (default):
#tuning_precision = 2
# a value of 1 selects 10^1 = 10Hz tuning precision:
#tuning_precision = 1

# This setting tells the auto-squelch the offset to add to the current signal level to use as the new squelch level.
# Lowering this setting will give you a more sensitive squelch, but it may also cause unwanted squelch openings when
# using the auto squelch.
#squelch_auto_margin = 10  # in dB

#google_maps_api_key = ""

# how long should positions be visible on the map?
# they will start fading out after half of that
# in seconds; default: 2 hours
#map_position_retention_time = 2 * 60 * 60

# decoder queue configuration
# due to the nature of some operating modes (ft8, ft8, jt9, jt65, wspr and js8), the data is recorded for a given amount
# of time (6 seconds up to 2 minutes) and decoded at the end. this can lead to very high peak loads.
# to mitigate this, the recordings will be queued and processed in sequence.
# the number of workers will limit the total amount of work (one worker will losely occupy one cpu / thread)
#decoding_queue_workers = 2
# the maximum queue length will cause decodes to be dumped if the workers cannot keep up
# if you are running background services, make sure this number is high enough to accept the task influx during peaks
# i.e. this should be higher than the number of decoding services running at the same time
#decoding_queue_length = 10

# wsjt decoding depth will allow more results, but will also consume more cpu
#wsjt_decoding_depth = 3
# can also be set for each mode separately
# jt65 seems to be somewhat prone to erroneous decodes, this setting handles that to some extent
#wsjt_decoding_depths = {"jt65": 1}

# FST4 can be transmitted in different intervals. This setting determines which intervals will be decoded.
# available values (in seconds): 15, 30, 60, 120, 300, 900, 1800
#fst4_enabled_intervals = [15, 30]

# FST4W can be transmitted in different intervals. This setting determines which intervals will be decoded.
# available values (in seconds): 120, 300, 900, 1800
#fst4w_enabled_intervals = [120, 300]

# Q65 allows many combinations of intervals and submodes. This setting determines which combinations will be decoded.
# Please use the mode letter followed by the decode interval in seconds to specify the combinations. For example:
#q65_enabled_combinations = ["A30", "E120", "C60"]

# JS8 comes in different speeds: normal, slow, fast, turbo. This setting controls which ones are enabled.
#js8_enabled_profiles = ["normal", "slow"]
# JS8 decoding depth; higher value will get more results, but will also consume more cpu
#js8_decoding_depth = 3

# Enable background service for decoding digital data. You can find more information at:
# https://github.com/jketterl/openwebrx/wiki/Background-decoding
#services_enabled = True
#services_decoders = ["ft8", "ft4", "wspr", "packet"]

# === aprs igate settings ===
# If you want to share your APRS decodes with the aprs network, configure these settings accordingly.
# Make sure that you have set services_enabled to true and customize services_decoders to your needs.
#aprs_callsign = "N0CALL"
#aprs_igate_enabled = False
#aprs_igate_server = "euro.aprs2.net"
#aprs_igate_password = ""
# beacon uses the receiver_gps setting, so if you enable this, make sure the location is correct there
#aprs_igate_beacon = False

# Uncomment the following to customize gateway beacon details reported to the aprs network
#   Plese see Dire Wolf's documentation on PBEACON configuration for complete details:
#   https://github.com/wb2osz/direwolf/raw/master/doc/User-Guide.pdf 

# Symbol in its two-character form as specified by the APRS spec at http://www.aprs.org/symbols/symbols-new.txt
#   Default: Receive only IGate (do not send msgs back to RF)  
# aprs_igate_symbol = "R&"

# Custom comment about igate 
#   Default: OpenWebRX APRS gateway
# aprs_igate_comment = "OpenWebRX APRS gateway"

# Antenna Height and Gain details
#   Unspecified by default
# Antenna height above average terrain (HAAT) in meters 
# aprs_igate_height = "5"
# Antenna gain in dBi
# aprs_igate_gain = "0"
# Antenna direction (N, NE, E, SE, S, SW, W, NW).  Omnidirectional by default
# aprs_igate_dir = "NE"

# === PSK Reporter settings ===
# enable this if you want to upload all ft8, ft4 etc spots to pskreporter.info
# this also uses the receiver_gps setting from above, so make sure it contains a correct locator
#pskreporter_enabled = False
#pskreporter_callsign = "N0CALL"
# optional antenna information, uncomment to enable
#pskreporter_antenna_information = "Dipole"

# === WSPRNet reporting settings
# enable this if you want to upload WSPR spots to wsprnet.ort
# in addition to these settings also make sure that receiver_gps contains your correct location
#wsprnet_enabled = False
#wsprnet_callsign = "N0CALL"
