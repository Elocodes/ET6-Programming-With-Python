import unittest

from ..mystery_7 import list_in_list

class TestMystery7(unittest.TestCase):
    """Test the list_in_list function"""

    def list_in_list(arg, b):
        """throw error if a is not a list of lists"""
        assert isinstance(arg, list)
        for sublists in arg:
            assert isinstance(sublists, list)

    def test_1(self):
        """it appends sublist to c if b is found in it"""
        actual = list_in_list([[9], [23, 8], ["apple"]], "apple")
        expected = [["apple"]]
        self.assertEqual(actual, expected)

    def test_2(self):
        """it appends sublist of multiple values to c if b is found in it"""
        actual = list_in_list([[9], [23, 8], ["apple", "cake", "jam"]], "apple")
        expected = [["apple", "cake", "jam"]]
        self.assertEqual(actual, expected)

    def test_3(self):
        """it appends sublists to c if b is found in more than one"""
        actual = list_in_list([[9, "apple"], [23, 8], ["apple", "cake", "jam"]], "apple")
        expected = [[9, "apple"], ["apple", "cake", "jam"]]
        self.assertEqual(actual, expected)

    def test_4(self):
        """it returns an empty list if b is not found among the sublists"""
        actual = list_in_list([[9], [23, 8], ["apple", "cake", "jam"]], "spinach")
        expected = []
        self.assertEqual(actual, expected)