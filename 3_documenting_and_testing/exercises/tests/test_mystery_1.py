import unittest

from ..mystery_1 import sum_of_numbers

class TestMystery1(unittest.TestCase):
    """Test the sum_of_numbers function"""

    def test_0(self):
        """it should throw an error if non integer is passed as argument"""
        with self.assertRaises(AssertionError):
            sum_of_numbers("9", 9)

    def test_1(self):
        """it should return a positive when a and b are positive"""
        actual = sum_of_numbers(700, 59)
        expected = 759
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should return a negative when the bigger argument has a negative value"""
        actual = sum_of_numbers(-700, 59)
        expected = -641
        self.assertEqual(actual, expected)

    def test_3(self):
        """it should sum floats"""
        actual = sum_of_numbers(0.78, 2.811)
        expected = 3.591
        self.assertEqual(actual, expected)

    def test_4(self):
        """it should sum zeros"""
        actual = sum_of_numbers(0, 0)
        expected = 0
        self.assertEqual(actual, expected)


