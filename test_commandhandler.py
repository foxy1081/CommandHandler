# test_commandhandler.py
"""
Tests for CommandHandler module.
"""

import unittest
from commandhandler import CommandHandler

class TestCommandHandler(unittest.TestCase):
    """Test cases for CommandHandler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CommandHandler()
        self.assertIsInstance(instance, CommandHandler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CommandHandler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
