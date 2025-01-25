#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_normal_case(self):
        """Test a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_case(self):
        """Test list of integers in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicates(self):
        """Test a list with duplicate elements."""
        self.assertEqual(max_integer([2, 3, 3, 2]), 3)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers."""
        self.assertEqual(max_integer([1, -1, 0, 2]), 2)

    def test_floats(self):
        """Test a list with floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 0.5]), 3.5)

    def test_all_negative_numbers(self):
        """Test a list with only negative numbers."""
        self.assertEqual(max_integer([-5, -10, -3]), -3)

if __name__ == '__main__':
    unittest.main()
