__author__ = 'Nikita Rybkin'

import unittest

from levenstein import dam_lev_dist as dist


class TestDomLev(unittest.TestCase):
    def test1(self):
        a = 'Lost'
        b = 'Ghost'
        self.assertEqual(dist(a, b), 3)

    def test2(self):
        a = 'Two sodas'
        b = 'Foos ro dah'
        self.assertEqual(dist(a, b), 6)

    def test3(self):
        a = 'It\'s alive'
        b = 'It\'s a lion'
        self.assertEqual(dist(a, b), 3)

    def test4(self):
        a = 'OneTwoThree'
        b = 'FourFiveSix'
        self.assertEqual(dist(a, b), 11)
