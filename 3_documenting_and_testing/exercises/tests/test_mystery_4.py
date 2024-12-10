import unittest

from ..mystery_4 import increment_list

class TestMystery4(unittest.TestCase):
    """Test the increment_list function"""

    def test_0(self):
        """raises an error if argument is a str"""
        with self.assertRaises(AssertionError):
            increment_list("i")

    def test_1(self):
        """it should return current state of b if len of b is equal to a"""
        actual = increment_list(0)
        expected = []
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should append the value of c to the list while len(list) is less than the argument value"""
        actual = increment_list(3)
        expected = [0, 1, 2]
        self.assertEqual(actual, expected)

    def test_3(self):
        """raises an error if argument is float"""
        with self.assertRaises(AssertionError):
            increment_list(9.2)

    def test_4(self):
        """raises an error if argument is a negative int"""
        with self.assertRaises(AssertionError):
            increment_list(-3)    

