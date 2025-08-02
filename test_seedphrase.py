# test_seedphrase.py
"""
Tests for SeedPhrase module.
"""

import unittest
from seedphrase import SeedPhrase

class TestSeedPhrase(unittest.TestCase):
    """Test cases for SeedPhrase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SeedPhrase()
        self.assertIsInstance(instance, SeedPhrase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SeedPhrase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
