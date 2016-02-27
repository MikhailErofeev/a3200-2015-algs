__author__ = 'Dmitry Petrushin'

import unittest

from pythagorean import *

class TestPythagorean(unittest.TestCase):
    def test_empty(self):
        array = []
        res = find_count_of_triples(array)
        expected = 0
        self.assertEqual(expected, res)

    def test_primitive(self):
        array = [3, 4, 5]
        res = find_count_of_triples(array)
        expected = 1
        self.assertEqual(expected, res)

    def test_main(self):
        array = [23, 247, 19, 96, 264, 265, 132, 265, 181]
        res = find_count_of_triples(array)
        expected = 2
        self.assertEqual(expected, res)

    def test(self):
        array = [3, 4, 5, 7, 9, 11, 12, 13, 15, 17, 24, 25, 40, 41, 60, 61, 84, 85, 112, 113, 144, 145]
        res = find_count_of_triples(array)
        expected = 9
        self.assertEqual(expected, res)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPythagorean)
    unittest.TextTestRunner(verbosity=2).run(suite)
