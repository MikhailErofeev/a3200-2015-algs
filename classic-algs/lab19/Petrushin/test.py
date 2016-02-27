__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest

from palindrome import palindrome as do


class TestPalindrome(unittest.TestCase):
    def test1(self):
        string = 'abca'
        res = do(string)
        exp = 'aba'
        self.assertEqual(res, exp)

    def test2(self):
        string = 'babcad'
        res = do(string)
        exp = 'bab'
        self.assertEqual(res, exp)

    def test3(self):
        string = 'KUULILENNUTEETUNNELILUUK'
        res = do(string)
        exp = 'KUULILENNUTEETUNNELILUUK'
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
