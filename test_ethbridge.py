# test_ethbridge.py
"""
Tests for EthBridge module.
"""

import unittest
from ethbridge import EthBridge

class TestEthBridge(unittest.TestCase):
    """Test cases for EthBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EthBridge()
        self.assertIsInstance(instance, EthBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EthBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
