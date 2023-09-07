#!/usr/bin/python3
'''
Using Unittest
'''
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ord_list(self):
        '''
        test a list that is order before
        '''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_inv_ord_list(self):
        '''
        test a list that is in inverse order before
        '''
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_no_ord_list(self):
        '''
        test a list that is not in order before
        '''
        self.assertEqual(max_integer([2, 8, 3, 1]), 8)

    def test_ord_list_neg(self):
        '''
        test a list that is not in order before
        '''
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_no_ord_list_neg(self):
        '''
        test a list that is not in order before
        '''
        self.assertEqual(max_integer([-2, -8, -3, -1]), -1)

    def test_no_ord_list_com(self):
        '''
        test a list that is not in order before
        '''
        self.assertEqual(max_integer([-2, 8, -3, -1]), 8)

    def test_ord_list_float(self):
        '''
        test a list that is order before
        '''
        self.assertEqual(max_integer([1.2, 2, 3.5, 4.6]), 4.6)

    def test_inv_ord_list_float(self):
        '''
        test a list that is in inverse order before
        '''
        self.assertEqual(max_integer([4.4, 3.2, 2, 1.4]), 4.4)

    def test_no_ord_list_float(self):
        '''
        test a list that is not in order before
        '''
        self.assertEqual(max_integer([2, 8.5, 3.6, 1.28]), 8.5)

    def test_string(self):
        '''
        test a list that is order before
        '''
        self.assertEqual(max_integer(['arm', 'bucle', 'kiwi']), 'kiwi')

    def test_unique(self):
        '''
        test a list that is just one element
        '''
        self.assertEqual(max_integer([4]), 4)

    def test_no_same_type(self):
        '''
        test a list that has two kinds
        '''
        with self.assertRaises(TypeError):
            max_integer([4, 'arm', 8])

    def test_nothing(self):
        '''
        test a list does not has something
        '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_nothing_t(self):
        '''
        test a list that is just one element
        '''
        self.assertEqual(max_integer([]), None)
