#!/usr/bin/python3
"""Unit tests for max_integer in list function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class contains unit tests for max_integer"""

    def test_positive(self):
        """Tests a list with no duplicates"""
        list_numbers = [1, 2, 5, 0, 3]
        self.assertEqual(max_integer(list_numbers), 5)

    def test_negative(self):
        """Tests a list with negative number"""
        list_numbers = [1, 2, 5, -6, 3]
        self.assertEqual(max_integer(list_numbers), 5)

    def test_negative_result(self):
        """Tests a list with negative number for the largest number"""
        list_numbers = [-1, -2, -5, -6, -3]
        self.assertEqual(max_integer(list_numbers), -1)

    def test_zero_result(self):
        """Tests a list with 0 as max"""
        list_numbers = [-1, 0, -5, -6, -3]
        self.assertEqual(max_integer(list_numbers), 0)

    def test_first(self):
        """Tests a list with the first element the maximum"""
        list_numbers = [10, 2, 5, -6, 3]
        self.assertEqual(max_integer(list_numbers), 10)

    def test_negative(self):
        """Tests a list with the last element the maximum"""
        list_numbers = [-10, -2, -5, -6, -1]
        self.assertEqual(max_integer(list_numbers), -1)

    def test_duplicate(self):
        """Tests a list with duplicate non-maximum values"""
        list_numbers = [1, -5, 3, 1, -5]
        self.assertEqual(max_integer(list_numbers), 3)

    def test_all_5000(self):
        """Tests a list with all values 5000"""
        list_numbers = [5000, 5000, 5000, 5000, 5000]
        self.assertEqual(max_integer(list_numbers), 5000)

    def test_all_0(self):
        """Tests a list with all values 0"""
        list_numbers = [0, 0, 0, 0, 0]
        self.assertEqual(max_integer(list_numbers), 0)

    def test_all_neg5000(self):
        """Tests a list with all values -5000"""
        list_numbers = [-5000, -5000, -5000, -5000, -5000]
        self.assertEqual(max_integer(list_numbers), -5000)

    def test_one_element(self):
        """Tests a list with one value -5000"""
        list_numbers = [-5000]
        self.assertEqual(max_integer(list_numbers), -5000)

    def test_empty(self):
        """Tests an empty list"""
        list_numbers = []
        self.assertIs(max_integer(list_numbers), None)

if __name__ == "__main__":
    unittest.main()
