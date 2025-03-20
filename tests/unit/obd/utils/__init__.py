from unittest import TestCase
from unittest.mock import patch

import obd.utils as utils


class TestOBDStatus(TestCase):
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
    def close(self):
        pass


class TestTryPort(TestCase):
    def setUp(self):
        self.portName = "testport"

    def test_try_port_fail(self):
        self.assertEqual(utils.try_port(self.portName), False)

    def test_try_port_success(self):
        with patch("serial.Serial") as mocked_port:
            mocked_port.return_value = MockSerialObjectWithClose()
            self.assertEqual(utils.try_port(self.portName), True)


class TestScanSerial(TestCase):
    def test_scan_serial_success(self):
        test = utils.scan_serial()
        self.assertIsInstance(test, list)
