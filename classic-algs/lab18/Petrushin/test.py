__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest

from Levenshtein import distance as do


class TestLevenshtein(unittest.TestCase):
    def test1(self):
        a = 'Levenshtien'
        b = 'Frankenstein'
        res = do(a, b)
        exp = 7
        self.assertEqual(res, exp)

    def test2(self):
        a = 'Petooshock'
        b = 'Toornickman'
        res = do(a, b)
        exp = 8
        self.assertEqual(res, exp)

    def test3(self):
        a = 'Assassin'
        b = 'Killer'
        res = do(a, b)
        exp = 8
        self.assertEqual(res, exp)

    def test4(self):
        a = 'GTA5'
        b = 'KurochkaRyaba'
        res = do(a, b)
        exp = 11
        self.assertEqual(res, exp)

    def test5(self):
        a = 'NepovtorimiyOriginal'
        b = 'ZhalkayaParodia'
        res = do(a, b)
        exp = 18
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
