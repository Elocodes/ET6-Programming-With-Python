import unittest

from ..mystery_2 import length_check

class TestMystery2(unittest.TestCase):
    """Test the length_check function"""

    def test_0(self):
        """it should raise an assertion error if argument is not str or list"""
        with self.assertRaises(AssertionError):
            length_check(79)

    def test_1(self):
        """it should return None if length of argument is 0"""
        actual = length_check("")
        expected = None
        self.assertEqual(actual, expected)

    def test_2(self):
        """it should return correct length of argument if str"""
        actual = length_check("education")
        expected = 9
        self.assertEqual(actual, expected)

    def test_3(self):
        """it should return correct length of argument if list"""
        actual = length_check([3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_4(self):
        """it should return correct length of argument if list with many values"""
        actual = length_check([3, 78, "bag"])
        expected = 3
        self.assertEqual(actual, expected)

    def test_5(self):
        """it should return correct length of argument if mixed with list of lists"""
        actual = length_check([[3], [45, 89], 8, 6])
        expected = 4
        self.assertEqual(actual, expected)

    def test_6(self):
        """it should return None if length of argument is 0 through empty list"""
        actual = length_check([])
        expected = None
        self.assertEqual(actual, expected)

    


