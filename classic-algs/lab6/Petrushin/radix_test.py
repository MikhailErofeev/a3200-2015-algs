__author__ = 'Dmitry Petrushin'

import unittest
from random import randint as rand

import radix


class TestSorting(unittest.TestCase):
    def test_empty(self):
        arr = []
        res = radix.extended_radix_sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_trivial(self):
        arr = [33, 22, 11, 0]
        res = radix.extended_radix_sort(arr)
        expected = [0, 11, 22, 33]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_mono_rank_length(self):
        arr = [rand(1000, 9999) for _ in range(1000)]
        res = radix.extended_radix_sort(arr)
        expected = sorted(arr)
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_multi_rank_length(self):
        arr = [rand(0, 10000) for _ in range(1000)]
        res = radix.extended_radix_sort(arr)
        expected = sorted(arr)
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_positive_long(self):
        arr = [rand(0, 1000000) for _ in range(1000000)]
        res = radix.extended_radix_sort(arr)
        expected = sorted(arr)
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_negative_long(self):
        arr = [rand(-1000000, 0) for _ in range(1000000)]
        res = radix.extended_radix_sort(arr)
        expected = sorted(arr)
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_different_long(self):
        arr = [rand(-1000000, 1000000) for _ in range(1000000)]
        res = radix.extended_radix_sort(arr)
        expected = sorted(arr)
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_sorted_positive(self):
        arr = sorted([rand(0, 1000000) for _ in range(1000)])
        res = radix.extended_radix_sort(arr)
        expected = arr
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_sorted_negative(self):
        arr = sorted([rand(-1000000, 0) for _ in range(1000)])
        res = radix.extended_radix_sort(arr)
        expected = arr
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_sorted_long(self):
        arr = sorted([rand(-1000000, 1000000) for _ in range(1000000)])
        res = radix.extended_radix_sort(arr)
        expected = arr
        self.assertFalse(not res)
        self.assertEqual(expected, res)
