import unittest

from ..list_to_list import list_to_list

class TestMystery5(unittest.TestCase):
    """Tests the list_to_list function"""

    def test_arg_type(self):
        """raises an error if argument is not iterable"""
        with self.assertRaises(AssertionError):
            list_to_list(500)

    def test_appends_numbers_smallest_to_biggest(self):
        """if a is a list of numbers, it should append the smallest value of a to the list b while a is not empty"""
        actual = list_to_list([-23, -67, -1])
        expected = [-67, -23, -1]
        self.assertEqual(actual, expected)

    def test_appends_str_alphabetically(self):
        """if a is list of striings, it should append the smallest value of a to the list b while a is not empty"""
        actual = list_to_list(["crab", "hill", "ballons", "break"])
        expected = ["ballons", "break", "crab", "hill"]
        self.assertEqual(actual, expected)

    def test_nested_lists(self):
        """if a is a list of lists, it should compare the inner lists based on the first element"""
        actual = list_to_list([[-23, 67, -1], [4, 3], [0]])
        expected = [[-23, 67, -1], [0], [4, 3]] 
        self.assertEqual(actual, expected)

    def test_mixed_values(self):
        """raises an error if argument is a list mixed with numbers and strings"""
        with self.assertRaises(AssertionError):
            list_to_list([3, 90, "dog"])

    def test_arg_passed(self):
        """raises an error if argument is a string"""
        with self.assertRaises(AssertionError):
            list_to_list("crab")

    
