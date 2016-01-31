__author__ = 'Nikita Rybkin'

import unittest

import dijkstra


class TestDjkstra(unittest.TestCase):
    def test_simple(self):
        graph = dijkstra.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_direct_link(2, 3, 4)
        graph.add_direct_link(0, 1, 2)
        graph.add_direct_link(1, 2, 1)
        graph.add_direct_link(3, 2, 8)
        res = graph.paths(0)
        expected = [0, 2, 3, None]
        self.assertEquals(expected, res)

    def test_the_simplest(self):
        graph = dijkstra.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_direct_link(0, 1, 15)
        res = graph.paths(0)
        expected = [0, 15]
        self.assertEquals(expected, res)

    def test_lection(self):
        graph = dijkstra.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_direct_link(0, 1, 10)
        graph.add_direct_link(0, 4, 5)
        graph.add_direct_link(1, 2, 1)
        graph.add_direct_link(1, 4, 2)
        graph.add_direct_link(2, 3, 4)
        graph.add_direct_link(3, 2, 6)
        graph.add_direct_link(3, 0, 7)
        graph.add_direct_link(4, 1, 3)
        graph.add_direct_link(4, 2, 9)
        graph.add_direct_link(4, 3, 2)
        res = graph.paths(0)
        expected = [0, 8, 9, 7, 5]
        self.assertEquals(expected, res)