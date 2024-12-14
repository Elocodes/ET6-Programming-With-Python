import unittest

from ..length_check import length_check

class TestLengthCheck(unittest.TestCase):
    """Test the length_check function"""

    def test_arg_type(self):
        """it should raise an assertion error if argument is not str or list"""
        with self.assertRaises(AssertionError):
            length_check(79)

    def test_empty_string(self):
        """it should return None if length of argument is 0"""
        actual = length_check("")
        expected = None
        self.assertEqual(actual, expected)

    def test_str(self):
        """it should return correct length of argument if str"""
        actual = length_check("education")
        expected = 9
        self.assertEqual(actual, expected)

    def test_list(self):
        """it should return correct length of argument if list"""
        actual = length_check([3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_multiple_values(self):
        """it should return correct length of argument if list with many values"""
        actual = length_check([3, 78, "bag"])
        expected = 3
        self.assertEqual(actual, expected)

    def test_nested_list(self):
        """it should return correct length of argument if mixed with list of lists"""
        actual = length_check([[3], [45, 89], 8, 6])
        expected = 4
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """it should return None if length of argument is 0 through empty list"""
        actual = length_check([])
        expected = None
        self.assertEqual(actual, expected)

    


