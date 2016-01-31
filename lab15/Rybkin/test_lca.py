__author__ = 'Nikita_Rybkin'

import unittest

from leastcommonancestor import Tree


class Tester(unittest.TestCase):
    def test1(self):
        a = [(0, 6), (3, 6), (6, 2), (4, 2), (1, 4), (5, 1), (7, 1)]
        tree = Tree(8, a, 2)
        self.assertEqual(tree.least_common_ancestor(0, 7), 2)
        self.assertEqual(tree.least_common_ancestor(5, 1), 1)
        self.assertEqual(tree.least_common_ancestor(1, 5), 1)
        self.assertEqual(tree.least_common_ancestor(0, 3), 6)

    def test2(self):
        a = [(0, 1)]
        tree = Tree(2, a, 1)
        self.assertEqual(tree.least_common_ancestor(0, 1), 1)
        self.assertEqual(tree.least_common_ancestor(1, 0), 1)
        self.assertEqual(tree.least_common_ancestor(0, 0), 0)
        self.assertEqual(tree.least_common_ancestor(1, 1), 1)

    def test3(self):
        a = [(0, 1), (0, 5), (1, 2), (1, 4), (2, 3)]
        tree = Tree(6, a, 0)
        self.assertEqual(tree.least_common_ancestor(0, 0), 0)
        self.assertEqual(tree.least_common_ancestor(1, 1), 1)
        self.assertEqual(tree.least_common_ancestor(3, 2), 2)
        self.assertEqual(tree.least_common_ancestor(1, 5), 0)
        self.assertEqual(tree.least_common_ancestor(3, 4), 1)
        self.assertEqual(tree.least_common_ancestor(3, 5), 0)

    def test4(self):
        n = 20
        root = 7
        a = [(7, 5), (7, 13), (7, 11), (11, 4), (11, 19), (4, 6), (4, 0), (4, 1), (4, 3), (13, 15), (13, 14),
             (15, 16), (16, 17), (16, 18), (5, 2), (2, 8), (8, 9), (8, 12), (8, 10)]
        tree = Tree(20, a, 7)
        self.assertEqual(tree.least_common_ancestor(5, 13), 7)
        self.assertEqual(tree.least_common_ancestor(6, 19), 11)
        self.assertEqual(tree.least_common_ancestor(6, 12), 7)
        self.assertEqual(tree.least_common_ancestor(15, 10), 7)
        self.assertEqual(tree.least_common_ancestor(18, 14), 13)
