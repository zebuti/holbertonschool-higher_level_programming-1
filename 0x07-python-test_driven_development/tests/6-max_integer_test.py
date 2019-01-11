#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer
    """

    def unit_passer(self):
        pass

    def max_int_basic(self):
        """tests normal list of ints
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def max_int_empty(self):
        """tests if list is empty
        """
        self.assertEqual(max_integer([]), None)

    def max_int_neg(self):
        """tests if list has a negative int
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def max_int_one(self):
        self.assertEqual(max_integer([1]), 1)
