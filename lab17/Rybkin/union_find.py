__author__ = 'Nikita Rybkin'


class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def creation(self, obj):
        self.parent[obj] = obj
        self.rank[obj] = 0

    def search(self, obj):
        if obj == self.parent[obj]:
            return obj
        self.parent[obj] = self.search(self.parent[obj])
        return self.parent[obj]

    def union_sets(self, obj1, obj2):
        n = self.search(obj1)
        m = self.search(obj2)
        if n != m:
            if self.rank[n] < self.rank[m]:
                n, m = m, n
            self.parent[m] = n
            if self.rank[n] == self.rank[m]:
                self.rank[n] += 1