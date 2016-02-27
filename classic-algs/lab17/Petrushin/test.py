__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest

from kruskal import WeightedGraph as G


class TestKruskal(unittest.TestCase):
    def test_empty(self):
        graph = G()
        expected = '[]'
        result = str(graph.min_tree())
        self.assertEqual(expected, result)

    def test_lecture(self):
        graph = G()
        for i in range(1, 10):
            graph.add_vertex(i)
        graph.add_direct_link(1, 2, 4)
        graph.add_direct_link(1, 8, 8)
        graph.add_direct_link(2, 3, 8)
        graph.add_direct_link(2, 8, 11)
        graph.add_direct_link(3, 4, 7)
        graph.add_direct_link(3, 6, 4)
        graph.add_direct_link(3, 9, 2)
        graph.add_direct_link(4, 5, 9)
        graph.add_direct_link(4, 6, 14)
        graph.add_direct_link(5, 6, 10)
        graph.add_direct_link(6, 7, 2)
        graph.add_direct_link(7, 8, 1)
        graph.add_direct_link(7, 9, 6)
        graph.add_direct_link(8, 9, 7)
        expected = '[[8, 2], [], [9, 4, 6], [5], [], [7], [8], [], []]'
        result = str(graph.min_tree())
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
