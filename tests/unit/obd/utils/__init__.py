import os
import sys
import re
from unittest import TestCase
from unittest.mock import patch

import obd.utils as utils


class TestOBDStatus(TestCase):
    """
    Regression catcher more than anything.
    """

    def setUp(self):
        self.status = utils.OBDStatus()

    def test_NotConnected(self):
        self.assertEqual(self.status.NOT_CONNECTED, "Not Connected")

    def test_ELMConnected(self):
        self.assertEqual(self.status.ELM_CONNECTED, "ELM Connected")

    def test_OBDConnected(self):
        self.assertEqual(self.status.OBD_CONNECTED, "OBD Connected")

    def test_CarConnected(self):
        self.assertEqual(self.status.CAR_CONNECTED, "Car Connected")


class MockSerialObjectWithClose:
    """
    To test try_port we just need an
    object that can close(). Close
    doesn't actually have to do
    anything.
    """
    def close(self):
        pass


class TestTryPort(TestCase):
    def setUp(self):
        self.portName = "bogustestport"

    def test_try_port_fail(self):
        self.assertEqual(utils.try_port(self.portName, debugOutput=False), False)

    def test_try_port_success(self):
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
    def setUp(self):
        self.linux_port_regexes = [
            "/dev/rfcomm[0-9]*",
            "/dev/ttyUSB[0-9]*",
            "/dev/ttyS[0-9]*",
            "/dev/ttyACM[0-9]*"
        ]
        self.win32_port_regexes = [
                "COM%d" % i for i in range(256)
        ]
        
        self.mac_port_regexes = [
            "/dev/tty.*(?=[^B][^l])"
        ]

    def test_scan_serial_success(self):
        test = utils.scan_serial(debugOutput=False)
        self.assertIsInstance(test, list)


    def test_scan_serial_linux(self):
        if sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(all_items_match_regexes(test, self.linux_port_regexes), True)
    
    def test_scan_serial_win(self):
        if sys.platform.startswith("win"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(all_items_match_regexes(test, self.win32_port_regexes), True)
    
    def test_scan_serial_mac(self):
        if sys.platform.startswith("darwin"):
            with patch("serial.Serial") as mocked_port:
                mocked_port.return_value = MockSerialObjectWithClose()
                test = utils.scan_serial(debugOutput=False)
                self.assertEqual(all_items_match_regexes(test, self.mac_port_regexes), True)
