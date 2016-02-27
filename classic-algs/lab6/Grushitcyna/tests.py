import unittest
import radix
import random


class TestSorting(unittest.TestCase):
    def test_trivial(self):
        arr = [1, 333, 22]
        res = radix.radix_sort(arr)
        expected = [1, 22, 333]
        self.assertFalse(not res)  # check res not empty
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = radix.radix_sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_reversed(self):
        arr = [5, 4, 3, 2, 1]
        res = radix.radix_sort(arr)
        expected = [1, 2, 3, 4, 5]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_sorted(self):
        arr = [1, 2, 3]
        res = radix.radix_sort(arr)
        expected = [1, 2, 3]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_random(self):
        arr = [random.randint(0, 100) for i in range(random.randint(0, 10))]
        res = radix.radix_sort(arr)
        arr.sort()
        self.assertFalse(not res)
        self.assertEqual(arr, res)
        
    def test_very_big(self):
        arr = [random.randint(0, 100) for i in range(10000)]
        res = radix.radix_sort(arr)
        arr.sort()
        self.assertFalse(not res)
        self.assertEqual(arr, res)
        
    def test_partially_sorted(self):
        arr = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        res = radix.radix_sort(arr)
        expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        self.assertFalse(not res)
        self.assertEqual(expected, res)
