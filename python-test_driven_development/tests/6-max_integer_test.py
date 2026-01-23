#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Docstring for TestMaxInteger
    """

    def test_empty_list(self):
        """
        Test an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """
        Test a list with duplicate maximum values
        """
        self.assertEqual(max_integer([1, 11, 11, 2]), 11)

    def test_single_number(self):
        """
        Test a single number in a list
        """
        self.assertEqual(max_integer([1]), 1)

    def test_negative_numbers(self):
        """
        Test a list with negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_positive_numbers(self):
        """
        Test a list with positive numbers
        """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """
        Test a list where the max is at the beginning
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """
        Test a list where the max is at the end
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_zero_in_list(self):
        """
        Test a list with zero included
        """
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_very_large_numbers(self):
        """
        Test a list with very large numbers
        """
        self.assertEqual(
            max_integer([999999999999, 8888888888888, 77777777777777]),
            77777777777777)

    def test_wrong_type(self):
        """
        Test a list with mixed types
        """
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_floats(self):
        """
        Test a list with float numbers
        """
        self.assertEqual(max_integer([1.5, 2.5, 0.5, 3.5]), 3.5)
