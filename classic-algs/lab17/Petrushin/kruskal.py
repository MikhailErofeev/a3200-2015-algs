__author__ = 'Dmitry Petrushin'
__version__ = '3.4'

from union_find import DSU


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
        dsu = DSU()
        edges = list()
        for v in self.vertexes.keys():
            dsu.make_set(v)
            a.add_vertex(v)
            for vertex in self.vertexes[v]:
                edges.append((self.vertexes[v][vertex], (v, vertex)))
        for (_, (u, v)) in sorted(edges):
            if dsu.find_set(u) != dsu.find_set(v):
                a.add_direct_link(u, v, self.vertexes[u][v])
                dsu.union_sets(u, v)
        return a

    def __str__(self):
        return str([self.get_links(v) for v in self.vertexes.keys()])


if __name__ == '__main__':
    pass
