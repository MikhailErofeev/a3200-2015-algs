__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest

from rectangle import rectangles as do


class TestRectangles(unittest.TestCase):
    def test1(self):
        lengths = list(map(int, '2 4 4 2'.split()))
        res = do(lengths)
        exp = 8
        self.assertEqual(res, exp)

    def test2(self):
        lengths = list(map(int, '2 2 3 5'.split()))
        res = do(lengths)
        exp = 0
        self.assertEqual(res, exp)

    def test3(self):
        lengths = list(map(int, '100003 100004 100005 100006'.split()))
        res = do(lengths)
        exp = 10000800015
        self.assertEqual(res, exp)

    def test4(self):
        lengths = list(map(int, '5 3 3 3 3 4 4 4'.split()))
        res = do(lengths)
        exp = 25
        self.assertEqual(res, exp)

    def test5(self):
        lengths = list(map(int, '123 124 123 124 2 2 2 2 9 9'.split()))
        res = do(lengths)
        exp = 15270
        self.assertEqual(res, exp)

    def test6(self):
        lengths = list(map(int, '10 10 10 10 11 10 11 10'.split()))
        res = do(lengths)
        exp = 210
        self.assertEqual(res, exp)

    def test7(self):
        lengths = list(map(int, '1000000'.split()))
        res = do(lengths)
        exp = 0
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
