import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from scans.arp_scan import arp_scan

class TestArpScan(unittest.TestCase):

    def test_arp_scan_valid_ip(self):
        # Test ARP scan on a valid IP range
        result = arp_scan("192.168.1.1/24")
        self.assertIsInstance(result, list) # Make sure the result is in list
        self.assertGreater(len(result), 0) # Ckeck for empty list

    def test_arp_scan_invalid_ip(self):
        # Test ARP scan on an invalid IP range
        result = arp_scan("192.168.999.1/24")
        self.assertEqual(result, []) # Ensure result of ARP scan is empty for an invalid IP

    def test_arp_scan_no_devices(self):
        # Test ARP scan with no devices found
        result = arp_scan("192.168.2.1/24") # Assuming no devices in this range
        self.assertEqual(result, []) # No devices should be found

if __name__ == "__main__":
    unittest.main()