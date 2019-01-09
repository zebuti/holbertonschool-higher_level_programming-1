#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer
    """
    def max_int_basic(self):
        """tests normal list of ints
        """
        test = [1, 2, 3, 4]
        self.assertEqual(max_integer(test), 4)

    def max_int_empty(self):
        """tests if list is empty
        """
        test = []
        self.assertEqual(max_integer(test), None)

    def max_int_neg(self):
        """tests if list has a negative int
        """
        test = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test), -1)

    def max_int_nonint(self):
        """tests if list has a non int variable
        """
        test = ['h', 2, 3, 4]
        with self.assertRaises(TypeError):
            max_integer(test)

if __name__ == '__main__':
    unittest.main()
