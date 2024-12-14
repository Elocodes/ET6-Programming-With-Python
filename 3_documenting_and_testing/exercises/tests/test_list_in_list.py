import unittest

from ..list_in_list import list_in_list

class TestMystery7(unittest.TestCase):
    """Test the list_in_list function"""

    def test_nested_list(self):
        """throw error if a is not a list containing other iterables - list or tuple"""
        with self.assertRaises(AssertionError):
            list_in_list([34, 8, 9], 8)

    def test_appends_single_list(self):
        """it appends sublist to c if b is found in it"""
        actual = list_in_list([[9], [23, 8], ["apple"]], "apple")
        expected = [["apple"]]
        self.assertEqual(actual, expected)

    def test_all_values_of_sublist(self):
        """it appends sublist of multiple values to c if b is found in it"""
        actual = list_in_list([[9], [23, 8], ["apple", "cake", "jam"]], "apple")
        expected = [["apple", "cake", "jam"]]
        self.assertEqual(actual, expected)

    def test_found_in_more_than_one(self):
        """it appends sublists to c if b is found in more than one"""
        actual = list_in_list([[9, "apple"], [23, 8], ["apple", "cake", "jam"]], "apple")
        expected = [[9, "apple"], ["apple", "cake", "jam"]]
        self.assertEqual(actual, expected)

    def test_not_found(self):
        """it returns an empty list if b is not found among the sublists"""
        actual = list_in_list([[9], [23, 8], ["apple", "cake", "jam"]], "spinach")
        expected = []
        self.assertEqual(actual, expected)