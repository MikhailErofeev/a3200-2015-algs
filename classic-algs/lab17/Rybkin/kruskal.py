__author__ = 'Nikita Rybkin'

from union_find import UnionFind


class WeightedGraph:
    def __init__(self):
        self.vertexes = dict()

    def add_vertex(self, v):
        self.vertexes[v] = dict()

    def add_direct_link(self, v1, v2, weight):
        self.vertexes[v1][v2] = weight

    def get_links(self, v):
        return list(self.vertexes[v])

    def min_tree(self):
        a = WeightedGraph()
        union_obj = UnionFind()
        edges = list()
        for vertex in self.vertexes.keys():
            union_obj.creation(vertex)
            a.add_vertex(vertex)
            for v in self.vertexes[vertex]:
                edges.append((self.vertexes[vertex][v], (vertex, v)))
        for (_, (ver, vertex)) in sorted(edges):
            if union_obj.search(ver) != union_obj.search(vertex):
                a.add_direct_link(ver, vertex, self.vertexes[ver][vertex])
                union_obj.union_sets(ver, vertex)
        return a

    def __str__(self):
        return str([self.get_links(v) for v in self.vertexes.keys()])
