from owrx.property import PropertyLayer, PropertyDeleted
from unittest import TestCase
from unittest.mock import Mock


class PropertyLayerTest(TestCase):
    def testCreationWithKwArgs(self):
        pm = PropertyLayer(testkey="value")
        self.assertEqual(pm["testkey"], "value")

        # this should be synonymous, so this is rather for illustration purposes
        contents = {"testkey": "value"}
        pm = PropertyLayer(**contents)
        self.assertEqual(pm["testkey"], "value")

    def testKeyIsset(self):
        pm = PropertyLayer()
        self.assertFalse("some_key" in pm)

    def testKeyError(self):
        pm = PropertyLayer()
        with self.assertRaises(KeyError):
            x = pm["some_key"]

    def testSubscription(self):
        pm = PropertyLayer()
        pm["testkey"] = "before"
        mock = Mock()
        pm.wire(mock.method)
        pm["testkey"] = "after"
        mock.method.assert_called_once_with({"testkey": "after"})

    def testUnsubscribe(self):
        pm = PropertyLayer()
        pm["testkey"] = "before"
        mock = Mock()
        sub = pm.wire(mock.method)
        pm["testkey"] = "between"
        mock.method.assert_called_once_with({"testkey": "between"})

        mock.reset_mock()
        pm.unwire(sub)
        pm["testkey"] = "after"
        mock.method.assert_not_called()

    def testContains(self):
        pm = PropertyLayer()
        pm["testkey"] = "value"
        self.assertTrue("testkey" in pm)

    def testDoesNotContain(self):
        pm = PropertyLayer()
        self.assertFalse("testkey" in pm)

    def testSubscribeBeforeSet(self):
        pm = PropertyLayer()
        mock = Mock()
        pm.wireProperty("testkey", mock.method)
        mock.method.assert_not_called()
        pm["testkey"] = "newvalue"
        mock.method.assert_called_once_with("newvalue")

    def testEventPreventedWhenValueUnchanged(self):
        pm = PropertyLayer()
        pm["testkey"] = "testvalue"
        mock = Mock()
        pm.wire(mock.method)
        pm["testkey"] = "testvalue"
        mock.method.assert_not_called()

    def testDeletionIsSent(self):
        pm = PropertyLayer(testkey="somevalue")
        mock = Mock()
        pm.wireProperty("testkey", mock.method)
        mock.method.reset_mock()
        del pm["testkey"]
        mock.method.assert_called_once_with(PropertyDeleted)

    def testDeletionInGeneralWiring(self):
        pm = PropertyLayer(testkey="somevalue")
        mock = Mock()
        pm.wire(mock.method)
        del pm["testkey"]
        mock.method.assert_called_once_with({"testkey": PropertyDeleted})

    def testNoDeletionEventWhenPropertyDoesntExist(self):
        pm = PropertyLayer(otherkey="somevalue")
        mock = Mock()
        pm.wireProperty("testkey", mock.method)
        mock.method.reset_mock()
        with self.assertRaises(KeyError):
            del pm["testkey"]
        mock.method.assert_not_called()
