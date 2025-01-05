import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from scans.port_scan import tcp_scan, udp_scan

class TestPortScan(unittest.TestCase):

    def test_tcp_scan_valid_ports(self):
        # Test TCP scan on a valid IP and ports
        result = tcp_scan("192.168.1.1", [22, 80])
        self.assertIsInstance(result, list) # Make sure the result is in list
        self.assertGreater(len(result), 0) # Ensure open ports are found

    def test_tcp_scan_no_open_ports(self):
        # Test TCP scan when no ports are open
        result = tcp_scan("192.168.1.1", [8080, 9000]) # Assuming these ports are closed
        self.assertEqual(result, []) # No open ports should be found

    def test_udp_scan_valid_ports(self):
        # Test UDP scan on a valid IP and ports
        result = udp_scan("192.168.1.1", [53, 123])
        self.assertIsInstance(result, list) # Make sure the result is in list
        self.assertGreater(len(result), 0) # Ensure open ports are found

    def test_udp_scan_no_open_ports(self):
        # Test UDP scan when no ports are open
        result = udp_scan("192.168.1.1", [10000, 20000]) # Assuming these ports are closed
        self.assertEqual(result, []) # No open ports should be found

if __name__ == "__main__":
    unittest.main()