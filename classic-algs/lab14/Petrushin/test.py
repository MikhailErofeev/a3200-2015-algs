__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest

from topological import Graph as G


class TestTopological(unittest.TestCase):
    def test_cycle1(self):
        graph = G()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(5, 6)
        graph.add_directed_link(6, 6)
        res = graph.topological_sort()
        exp = None
        self.assertEqual(res, exp)

    def test_cycle2(self):
        graph = G()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(4, 2)
        graph.add_directed_link(2, 3)
        res = graph.topological_sort()
        exp = None
        self.assertEqual(res, exp)

    def test1(self):
        graph = G()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(5, 6)
        res = graph.topological_sort()
        exp = [1, 2, 4, 5, 6, 3]
        self.assertEqual(res, exp)

    def test2(self):
        graph = G()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(4, 2)
        res = graph.topological_sort()
        exp = [1, 3, 4, 2]
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
