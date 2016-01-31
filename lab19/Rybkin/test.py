__author__ = 'Nikita Rybkin'

from unittest import TestCase

from palindrome import palindrome


class Test(TestCase):
    def test1(self):
        self.assertEqual(palindrome("abca"), "aba")

    def test2(self):
        self.assertEqual(palindrome("babcad"), "bab")

    def empty_test(self):
        self.assertEqual(palindrome(""), "")

    def triv_test(self):
        self.assertEqual(palindrome("k"), "k")

    def triv_test2(self):
        self.assertEqual(palindrome("kf"), "k")

    def test3(self):
        self.assertEqual(palindrome("abacabazzzzzzz"), "abacaba")

    def test4(self):
        self.assertEqual(palindrome("a v enisee sineva"), "aveniseesineva")
