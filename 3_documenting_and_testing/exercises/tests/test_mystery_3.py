import unittest

from ..mystery_3 import min_or_equal

class TestMystery3(unittest.TestCase):
    """Test the min_or_equal function"""
    
    def test_0(self):
        """it should raise an assertion error if argument is not int"""
        with self.assertRaises(AssertionError):
            min_or_equal("math", "7")

    def test_1(self):
        """it should return the smallest number"""
        actual = min_or_equal(9, -1)
        expected = -1
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should return the sum of the number"""
        actual = min_or_equal(0, 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_3(self):
        """it should sum the floats"""
        self.assertEqual(min_or_equal(-0.3, -0.3), -0.6)
