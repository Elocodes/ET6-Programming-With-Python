import unittest

from ..mystery_6 import append_to_c

class TestMystery6(unittest.TestCase):
    """Test the append_to_c function"""

    def test_0(self):
        """it should raise an assertion error if argument is not int"""
        with self.assertRaises(AssertionError):
            append_to_c(2.5, 8)

    def test_1(self):
        """it evaluates to [] if a is equal to 0"""
        actual = append_to_c(0, 8)
        expected = []
        self.assertEqual(actual, expected)

    def test_2(self):
        """it appends to c if len of c is less than a"""
        actual = append_to_c(3, 8)
        expected = [8, 9, 10]
        self.assertEqual(actual, expected)

    
