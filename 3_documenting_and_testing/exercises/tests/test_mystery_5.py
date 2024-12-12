import unittest

from ..mystery_5 import list_to_list

class TestMystery5(unittest.TestCase):
    """Tests the list_to_list function"""

    def test_0(self):
        """raises an error if argument is not iterable"""
        with self.assertRaises(AssertionError):
            list_to_list(500)

    def test_1(self):
        """if a is a list of numbers, it should append the smallest value of a to the list b while a is not empty"""
        actual = list_to_list([-23, -67, -1])
        expected = [-67, -23, -1]
        self.assertEqual(actual, expected)

    def test_2(self):
        """if a is list of striings, it should append the smallest value of a to the list b while a is not empty"""
        actual = list_to_list(["crab", "hill", "ballons", "break"])
        expected = ["ballons", "break", "crab", "hill"]
        self.assertEqual(actual, expected)

    def test_3(self):
        """if a is a list of lists, it should compare the inner lists based on the first element"""
        actual = list_to_list([[-23, 67, -1], [4, 3], [0]])
        expected = [[-23, 67, -1], [0], [4, 3]] 
        self.assertEqual(actual, expected)

    def test_4(self):
        """raises an error if argument is a list mixed with numbers and strings"""
        with self.assertRaises(AssertionError):
            list_to_list([3, 90, "dog"])

    def test_5(self):
        """raises an error if argument is a string"""
        with self.assertRaises(AssertionError):
            list_to_list("crab")

    
