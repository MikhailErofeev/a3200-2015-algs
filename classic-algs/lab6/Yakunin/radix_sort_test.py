import unittest
import radix_sort
import random 


class TestSorting(unittest.TestCase):
    def is_sorted(self, arr):
        if len(arr) < 2:
            return True
        issorted = True
        for i in rannge(1, len(arr)):
            if arr[i] < arr[i - 1]:
                issorted = False
        return issorted
    
    def test_trivial(self):
        arr = [42, 23, 16, 15, 8, 4, 17, 13, 11, 7, 5, 3, 2]
        res = radix_sort.sort(arr)
        expected = [2, 3, 4, 5, 7, 8, 11, 13, 15, 16, 17, 23, 42]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = radix_sort.sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_random(self):
        random.seed()
        arr = []
        for i in range(random.randint(100, 1000)):
            arr.append(random.randint(-100000, 100000))
        res = radix_sort.sort(arr)
        self.assertTrue(is_sorted(res))

    def test_random_repeating(self):
        random.seed()
        arr = []
        for i in range(random.randint(10, 100)):
            val = random.randint(-100000, 100000)
            for j in range(random.randint(1, 15)):
                arr.append(val)
        res = radix_sort.sort(arr)
        self.assertTrue(is_sorted(res))
