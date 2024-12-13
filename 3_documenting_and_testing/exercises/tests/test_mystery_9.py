import unittest

from ..mystery_9 import sort_values

class TestMystery9(unittest.TestCase):
    """Test the sort_values function"""

    def test_arg_is_list(self):
        """it should throw error if arg passed is not a list"""
        with self.assertRaises(AssertionError):
            sort_values((89, 8))

    def test_0(self):
        """it swaps values if number is bigger than the value after it"""
        actual = sort_values([7, 3, 2])
        expected = [2, 3, 7]
        self.assertEqual(actual, expected)

    def test_1(self):
        """it does nothing if arg passed if already sorted"""
        actual = sort_values([5, 6, 7])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_2(self):
        """returns empty list if list passed is empty"""
        actual = sort_values([])
        expected = []
        self.assertEqual(actual, expected)
