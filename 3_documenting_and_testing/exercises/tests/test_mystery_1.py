import unittest

from ..mystery_1 import sum_of_numbers

class TestMystery1(unittest.TestCase):
    """Test the sum_of_numbers function"""

    def test_0(self):
        """it should throw an error if non integer is passed as argument a"""
        actual = sum_of_numbers("7", 90)
        expected = "argument must be an int"
        self.assertEqual(actual, expected)

    def test_1(self):
        """ it should throw an errror if argument b is non int"""
        actual = sum_of_numbers(4, "k")
        expected = "argument must be an int"
        self.assertEqual(actual, expected)

    def test_1(self):
        """ it should throw an errror if both arguments are non int"""
        actual = sum_of_numbers("4", "k")
        expected = "argument must be an int"
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should return a positive when a and b are positive"""
        actual = sum_of_numbers(700, 59)
        expected = 759
        self.assertEqual(actual, expected)

    def test_3(self):
        """it should return a negative when the bigger argument has a negative value"""
        actual = sum_of_numbers(-700, 59)
        expected = -641
        self.assertEqual(actual, expected)


