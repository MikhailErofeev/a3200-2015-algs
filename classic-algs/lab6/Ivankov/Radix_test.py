__author__ = 'Laz.Go'


import unittest
from random import randint as rand

import Radix

rad = Radix.eRadixSort()

class test_Sorting(unittest.TestCase):

    def test_Trivial(self):
        array = [33, 22, 11, 0]
        res = rad(array)
        exp = [0, 11, 22, 33]
        self.assertFalse(not res)
        self.assertEqual(exp, res)

    def test_MonoRankLength(self):
        array = [rand(1000, 9999) for _ in range(1000)]
        res = rad(array)
        exp = sorted(array)
        self.assertFalse(not res)
        self.assertEqual(exp, res)

    def test_MultiRankLength(self):
        array = [rand(0, 10000) for _ in range(1000)]
        res = rad(array)
        exp = sorted(array)
        self.assertFalse(not res)
        self.assertEqual(exp, res)


    def test_SortNegative(self):
        array = sorted([rand(-1000000, 0) for _ in range(1000)])
        res = rad(array)
        exp = array
        self.assertFalse(not res)
        self.assertEqual(exp, res)

    def test_SortLong(self):
        array = sorted([rand(-1000000, 1000000) for _ in range(1000000)])
        res = rad(array)
        exp = array
        self.assertFalse(not res)
        self.assertEqual(exp, res)

    def test_Empty(self):
        array = []
        res = rad(array)
        exp = []
        self.assertEqual(exp, res)