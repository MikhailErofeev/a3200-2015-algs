__author__ = 'Dmitry Petrushin'
__version__ = '3.4'


class DSU:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def make_set(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
