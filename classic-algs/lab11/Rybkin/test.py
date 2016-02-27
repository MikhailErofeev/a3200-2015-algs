__author__ = 'Nikita Rybkin'

import unittest

from barchart import bar_chart


class TestArea(unittest.TestCase):
    def test_empty(self):
        ans = bar_chart([])
        self.assertEqual(ans, 0)

    def test_one_elem(self):
        ans = bar_chart([68435654])
        self.assertEqual(ans, 0)

    def test_two_elem(self):
        ans = bar_chart([8384593849, -5365429])
        self.assertEqual(ans, 0)

    def test_twin_peaks(self):
        ans = bar_chart([1, 10, 0, 11, 2])
        self.assertEqual(ans, 10)

    def test_single_min(self):
        ans = bar_chart([8, 7, 5, 2, 2, 3, 2, 1, 2, 3, 10])
        self.assertEqual(ans, 45)

    def test_saw(self):
        arg = []
        for i in range(10000):
            arg.append(10)
            arg.append(9)
            arg.append(5)
            arg.append(9)
        ans = bar_chart(arg)
        self.assertEqual(ans, 7)

    def test_saw2(self):
        arg = [4, 9, 1]
        for i in range(10000):
            arg.append(10)
            arg.append(9)
            arg.append(5)
        ans = bar_chart(arg)
        self.assertEqual(ans, 8)

    def test_saw3(self):
        arg = [4, 9, 6]
        for i in range(10000):
            arg.append(10)
            arg.append(9)
            arg.append(5)
        ans = bar_chart(arg)
        self.assertEqual(ans, 6)

    def test_tricky_triple_saw(self):
        arg = []
        for i in range(10000):
            arg.append(100)
            arg.append(95)
            arg.append(80)
            arg.append(85)
            arg.append(70)
            arg.append(50)
            arg.append(40)
            arg.append(41)
            arg.append(45)
            arg.append(41)
            arg.append(40)
            arg.append(50)
            arg.append(70)
            arg.append(85)
            arg.append(80)
            arg.append(95)
            arg.append(100)
        ans = bar_chart(arg)
        self.assertEqual(ans, 533)

    def test_twin_tricky_triple_saw(self):
        arg = [0, -1000]
        for i in range(10000):
            arg.append(100)
            arg.append(95)
            arg.append(80)
            arg.append(85)
            arg.append(70)
            arg.append(50)
            arg.append(40)
            arg.append(41)
            arg.append(45)
            arg.append(41)
            arg.append(40)
            arg.append(50)
            arg.append(70)
            arg.append(85)
            arg.append(80)
            arg.append(95)
            arg.append(100)
        arg.append(0)
        arg.append(-999)
        ans = bar_chart(arg)
        self.assertEqual(ans, 1000)