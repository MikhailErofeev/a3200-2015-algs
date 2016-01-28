class Graph:
    def __init__(self):
        self.graph = {}
        self.flag = True

    '''white color == 1; green color == 2; blue color == 3.'''

    def add_vertex(self, v):
        self.graph[v] = [1]

    def add_direct_link(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, graph):
        arr = []
        self.flag = True
        for v in graph:
            if graph[v][0] == 1:
                self.DFS_visit(graph, graph[v], v, arr)
        if not self.flag:
            return None
        else:
            return list(reversed(arr))

    def DFS_visit(self, graph, vertex, key, arr):
        vertex[0] = 2
        for i in range(1, len(vertex)):
            if graph[vertex[i]][0] == 1:
                self.DFS_visit(graph, graph[vertex[i]], vertex[i], arr)
            elif graph[vertex[i]][0] == 2:
                self.flag = False
                break
        vertex[0] = 3
        arr.append(key)

    def topological_sort(self):
        return self.DFS(self.graph)


