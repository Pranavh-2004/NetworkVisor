import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from scans.ping_sweep import ping_sweep

class TestPingSweep(unittest.TestCase):

    def test_ping_sweep_valid_range(self):
        # Test Ping Sweep on a valid IP range
        result = ping_sweep("192.168.1.1/24")
        self.assertIsInstance(result, list) # Make sure the result is in list
        self.assertGreater(len(result), 0) # Ensure there are live hosts are found

    # def test_ping_sweep_invalid_range(self):
    #     # Test Ping Sweep on an invalid IP range
    #     result = ping_sweep("192.168.999.1/24")
    #     self.assertEqual(result, []) # No live hosts should be found for an invalid IP
    
    def test_ping_sweep_invalid_range(self):
        # Test Ping Sweep on an invalid IP range
        with self.assertRaises(ValueError):
            ping_sweep("192.168.999.1/24")  # Invalid IP should raise ValueError

    def test_ping_sweep_no_live_hosts(self):
        # Test Ping Sweep with no live hosts found
        result = ping_sweep("192.168.2.1/24") # Assuming no devices in this range
        self.assertEqual(result, []) # No live hosts should be found

if __name__ == "__main__":
    unittest.main()