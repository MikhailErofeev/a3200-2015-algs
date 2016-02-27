__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import unittest
from dijkstra import WeightedGraph


class TestDijkstra(unittest.TestCase):
    def test_trivial(self):
        graph = WeightedGraph()
        graph.add_vertex(10)
        graph.add_vertex(20)
        graph.add_vertex(30)
        graph.add_direct_link(10, 20, 100)
        graph.add_direct_link(10, 30, 1)
        graph.add_direct_link(30, 20, 2)
        res = graph.paths(10)
        expected = [0, 3, 1]
        self.assertEqual(res, expected)

    def test_lecture(self):
        graph = WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_direct_link(1, 2, 10)
        graph.add_direct_link(1, 5, 5)
        graph.add_direct_link(2, 3, 1)
        graph.add_direct_link(2, 5, 2)
        graph.add_direct_link(3, 4, 4)
        graph.add_direct_link(4, 3, 6)
        graph.add_direct_link(4, 1, 7)
        graph.add_direct_link(5, 4, 2)
        graph.add_direct_link(5, 3, 9)
        graph.add_direct_link(5, 2, 3)
        res = graph.paths(1)
        expected = [0, 8, 9, 7, 5]
        self.assertEqual(res, expected)

    def test_from_habr(self):
        '''http://habrahabr.ru/post/111361/'''
        graph = WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_direct_link(1, 2, 10)
        graph.add_direct_link(1, 3, 30)
        graph.add_direct_link(1, 4, 50)
        graph.add_direct_link(1, 5, 10)
        graph.add_direct_link(3, 5, 10)
        graph.add_direct_link(4, 2, 40)
        graph.add_direct_link(4, 3, 20)
        graph.add_direct_link(5, 1, 10)
        graph.add_direct_link(5, 3, 10)
        graph.add_direct_link(5, 4, 30)
        res = graph.paths(1)
        expected = [0, 10, 20, 40, 10]
        self.assertEqual(res, expected)

    def test_from_compscience(self):
        '''
        http://comp-science.narod.ru/KPG/Deikstr.htm
            but there is the problem in result
            i.e. their result for 1 -> 5 is 20, but it's impossible in given graph
        p.s. their graph is given by transforming not-oriented graph from
            https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%94%D0%B5%D0%B9%D0%BA%D1%81%D1%82%D1%80%D1%8B
            to oriented graph with an error, relied on grabbing an answer without checking
        '''
        graph = WeightedGraph()
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_direct_link(1, 2, 7)
        graph.add_direct_link(1, 3, 9)
        graph.add_direct_link(1, 6, 14)
        graph.add_direct_link(2, 3, 10)
        graph.add_direct_link(2, 4, 15)
        graph.add_direct_link(3, 6, 2)
        graph.add_direct_link(3, 4, 11)
        graph.add_direct_link(4, 5, 6)
        graph.add_direct_link(5, 6, 9)
        res = graph.paths(1)
        expected = [0, 7, 9, 20, 26, 11]
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()