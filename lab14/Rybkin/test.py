__author__ = 'Nikita Rybkin'

import unittest
import topologicalsort

class TestTopologicalSort(unittest.TestCase):

    def test_simple(self):
        graph = topologicalsort.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_direct_link(1, 3)
        graph.add_direct_link(3, 4)
        graph.add_direct_link(1, 2)
        graph.add_direct_link(4, 2)
        res = graph.topological_sort()
        expected = [1, 3, 4, 2]
        self.assertEquals(res, expected)

    def test_another_simple(self):
        graph = topological_sort.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_direct_link(1, 2)
        graph.add_direct_link(3, 1)
        res = graph.topological_sort()
        expected = [3, 1, 2]
        self.assertEquals(res, expected)

    def test_none(self):
        graph = topologicalsort.Graph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_direct_link(1, 3)
        graph.add_direct_link(4, 3)
        graph.add_direct_link(3, 4)
        graph.add_direct_link(1, 2)
        graph.add_direct_link(2, 3)
        graph.add_direct_link(4, 2)
        res = graph.topological_sort()
        expected = None
        self.assertEquals(res, expected)