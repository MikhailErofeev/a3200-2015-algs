__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

import heapq
from decimal import Decimal


class WeightedGraph():
    def __init__(self):
        self.vertexes = dict()
        self.INF = Decimal("Infinity")

    def add_vertex(self, v):
        self.vertexes[v] = dict()

    def add_direct_link(self, vertex1, vertex2, weight):
        self.vertexes[vertex1][vertex2] = weight

    def paths(self, vertex=None):
        d = dict()
        for i in self.vertexes:
            d[i] = self.INF
        d[vertex] = 0
        q = [(d[vertex], vertex) for vertex in self.vertexes]
        while len(q) != 0:
            heapq.heapify(q)
            _, u = heapq.heappop(q)
            for vertex in self.vertexes[u]:
                if d[vertex] > d[u] + self.vertexes[u][vertex]:
                    d[vertex] = d[u] + self.vertexes[u][vertex]
                    for i in range(len(q)):
                        x, y = q[i]
                        if y == vertex:
                            x = d[vertex]
                            q[i] = x, y
                            break
        return [None if d[vertex] == self.INF else d[vertex] for vertex in self.vertexes]


if __name__ == '__main__':
    pass