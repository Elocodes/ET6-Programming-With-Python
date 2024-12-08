import unittest

from ..mystery_2 import length_check

class TestMystery2(unittest.TestCase):
    """Test the length_check function"""

    def test_0(self):
        """it should raise an assertion error if argument is not str"""
        with self.assertRaises(AssertionError):
            length_check(79)

    def test_1(self):
        """it should return None if length of argument is 0"""
        actual = length_check()
        expected = None
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should return correct length of argument"""
        actual = length_check("education")
        expected = 9
        self.assertEqual(actual, expected)

