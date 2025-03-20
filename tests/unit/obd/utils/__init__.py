import os
import sys
import re
from unittest import TestCase
from unittest.mock import patch
from hypothesis import given, strategies as st

# Unit Under Test
import obd.utils as utils


class TestOBDStatus(TestCase):
    """
    Regression catcher more than anything.
    """

    def setUp(self):
        self.status = utils.OBDStatus()

    def testNotConnected(self):
        self.assertEqual(self.status.NOT_CONNECTED, "Not Connected")

    def testELMConnected(self):
        self.assertEqual(self.status.ELM_CONNECTED, "ELM Connected")

    def testOBDConnected(self):
        self.assertEqual(self.status.OBD_CONNECTED, "OBD Connected")

    def testCarConnected(self):
        self.assertEqual(self.status.CAR_CONNECTED, "Car Connected")


class TestBitArray(TestCase):
    pass


class TestBytesToInt(TestCase):
    @given(st.binary(min_size=2, max_size=256))
    def testBytesToIntSuccess(self, b):
        validate = int.from_bytes(b, byteorder="big")
        self.assertEqual(utils.bytes_to_int(b), validate)
    
    @given(st.binary(min_size=2, max_size=256))
    def testBytesToIntFail(self, b):
        validate = int.from_bytes(b, byteorder="little")
        """
        It doesn't look like the hypothesis binary
        strategy will let us exclude zero as a value.
        For that trivial case, we'll fail to fail.
        Other than that, we succeed on failing when
        our validator has the wrong byte order.
        """
        if validate > 0:
            self.assertNotEqual(utils.bytes_to_int(b), validate)


class TestBytesToHex(TestCase):
    pass


class MockSerialObjectWithClose:
    """
    To test `try_port` we just need an
    object that can close(). Close doesn't
    actually have to do anything.
    """

    def close(self):
        pass


class TestTryPort(TestCase):
    def setUp(self):
        self.portName = "bogustestport"

    def testTryPortFail(self):
        self.assertEqual(utils.try_port(self.portName, debugOutput=False), False)

    def testTryPortSuccess(self):
        with patch("serial.Serial") as mocked_port:
            mocked_port.return_value = MockSerialObjectWithClose()
            self.assertEqual(utils.try_port(self.portName, debugOutput=False), True)


def all_items_match_regexes(item_list, regex_list):
    """
    Checks if all items in a list match at least one regex in a list of regexes.

    Args:
      item_list: A list of strings to check.
      regex_list: A list of regex patterns.

    Returns:
      True if all items match at least one regex, False otherwise.
    """
    for item in item_list:
        if not any(re.search(regex, item) for regex in regex_list):
            return False
    return True


class TestScanSerial(TestCase):
    """
    Mildly irritating that patching sys.platform
    isn't as simple as it is for everything else.
    As it is, we can fallback on CI to execute
    each test case for us as long as we spin up
    a test on each platform and everything passes.
    """
    def setUp(self):
        self.linux_port_regexes = [
            "/dev/rfcomm[0-9]*",
            "/dev/ttyUSB[0-9]*",
            "/dev/ttyS[0-9]*",
            "/dev/ttyACM[0-9]*",
        ]
        self.win32_port_regexes = ["COM%d" % i for i in range(256)]
        # Negative lookahead for the Bluetooth ones we're excluding
        self.mac_port_regexes = ["/dev/tty.*(?=[^B][^l])"]

    def testScanSerialSuccess(self):
        test = utils.scan_serial(debugOutput=False)
        self.assertIsInstance(test, list)

    def testScanSerialLinux(self):
        if sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(
                    all_items_match_regexes(test, self.linux_port_regexes), True
                )

    def testScanSerialWin(self):
        if sys.platform.startswith("win"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(
                    all_items_match_regexes(test, self.win32_port_regexes), True
                )

    def testScanSerialMac(self):
        if sys.platform.startswith("darwin"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(
                    all_items_match_regexes(test, self.mac_port_regexes), True
                )
