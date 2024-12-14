import unittest

from ..loop_through_lists import loop_through_lists

class TestMystery8(unittest.TestCase):
    """Test the loop_through_lists function"""

    def test_arg_type(self):
        """throw error if a is not a list of lists"""
        with self.assertRaises(AssertionError):
            loop_through_lists([(67, 7), [7, 9]])

    def test_found_in_one(self):
        """it appends the sublist if b is found in it"""
        actual = loop_through_lists([[2, 9, 8], [56, 3], [4]], 9)
        expected = [[2, 9, 8]]
        self.assertEqual(actual, expected)

    def test_found_in_many(self):
        """it appends the sublists if b is found in more than one"""
        actual = loop_through_lists([[2, 9, 8], [56, 3], [4, 9]], 9)
        expected = [[2, 9, 8], [4, 9]]
        self.assertEqual(actual, expected)

    def test_not_found(self):
        """it returns and empty list if b is not found among the sublists"""
        actual = loop_through_lists([[2, 9, 8], [56, 3], [4, 9]], 10)
        expected = []
        self.assertEqual(actual, expected)
