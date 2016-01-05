import heapq


class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = 2**256
        self.parent = None
        self.weight = {}

    def __lt__(self, other):
        return self.distance < other.distance


class WeightedGraph:

    def __init__(self):
        self.graph = []

    def __str__(self):
        return str(self.graph)

    def add_vertex(self, v):
        self.graph.append(Vertex(v))

    def add_direct_link(self, v1, v2, weight):
        self.graph[v1].weight[v2] = weight

    def relax(self, u, v, weight):
        if self.graph[v].distance > self.graph[u].distance + weight:
            self.graph[v].distance = self.graph[u].distance + weight
            self.graph[v].parent = u

    def paths(self, w):
        S = []
        Q = []
        for vert in self.graph:
            if vert.name == w:
                vert.distance = 0
                vert.parent = w
            else:
                vert.distance = 2**256
                vert.parent = None
            heapq.heappush(Q, vert)
        while len(Q) != 0:
            u = heapq.heappop(Q)
            S.append(u)
            for v in u.weight:
                self.relax(u.name, v, u.weight[v])
        return [i.distance for i in self.graph]



