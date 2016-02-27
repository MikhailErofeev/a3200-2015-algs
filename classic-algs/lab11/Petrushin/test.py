__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest
from histogram import *


class TestHistogram(unittest.TestCase):
    def test_empty(self):
        hist = []
        res = MaxHistogram(hist).max_histograms_area()
        expected = 0
        self.assertEqual(res, expected)

    def test_main(self):
        hist = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        res = MaxHistogram(hist).max_histograms_area()
        expected = 10
        self.assertEqual(res, expected)

    def test_little(self):
        hist = [0, 10, 5, 10]
        res = MaxHistogram(hist).max_histograms_area()
        expected = 5
        self.assertEqual(res, expected)

    def test_big(self):
        hist = [0, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10,
                10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10, 10, 5, 10]
        res = MaxHistogram(hist).max_histograms_area()
        expected = 5
        self.assertEqual(res, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHistogram)
    unittest.TextTestRunner(verbosity=2).run(suite)
