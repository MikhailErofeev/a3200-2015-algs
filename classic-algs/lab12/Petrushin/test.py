__author__ = 'Dmitry Petrushin'

import unittest

from bst import *


def add_nodes(tree, array):
    for i in range(len(array)):
        tree.add(array[i])


class TestBST(unittest.TestCase):
    def test_empty(self):
        arr = []
        bst = UnbalancedBinarySearchTree()
        add_nodes(bst, arr)
        result = [i for i in bst]
        expected = []
        self.assertEqual(result, expected)

    def test_trivial(self):
        arr = [2, 4, 3, 1, 5]
        bst = UnbalancedBinarySearchTree()
        add_nodes(bst, arr)
        result = [i for i in bst]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_one_handed(self):
        arr = [1, 2, 3, 4, 5]
        bst = UnbalancedBinarySearchTree()
        add_nodes(bst, arr)
        result = [i for i in bst]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
    unittest.TextTestRunner(verbosity=2).run(suite)