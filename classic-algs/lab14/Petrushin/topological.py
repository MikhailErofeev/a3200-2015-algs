__author__ = 'Dmitry Petrushin'
__version__ = '3.4'


class Graph:
    class Color:
        def __init__(self):
            self.blue = 1
            self.green = 2
            self.white = 3

    def __init__(self):
        self.matrix = [list(), list()]
        self.colors = self.Color()
        self.order = list()
        self.visit = dict()
        self.k = 0

    def add_vertex(self, vertex):
        self.matrix[0] += [vertex]
        self.visit.update({vertex: self.colors.white})
        for i in range(1, len(self.matrix)):
            self.matrix[i] += [0]
        self.matrix += [[0] * len(self.matrix)]

    def add_directed_link(self, vertex1, vertex2):
        if self.matrix[self.matrix[0].index(vertex1) + 1][self.matrix[0].index(vertex2)] != 1:
            self.matrix[self.matrix[0].index(vertex1) + 1][self.matrix[0].index(vertex2)] = 1
        else:
            pass

    def dfs(self):
        for vertex, color in self.visit.items():
            if color == self.colors.white:
                self.special_dfs(vertex)

    def special_dfs(self, vertex):
        self.visit[vertex] = self.colors.green
        for vertice in self.visit.keys():
            condition = self.matrix[self.matrix[0].index(vertex) + 1][self.matrix[0].index(vertice)] == 1
            if self.visit[vertice] == self.colors.green and condition:
                self.k = None
                break
            if self.visit[vertice] == self.colors.white and condition:
                self.special_dfs(vertice)
        self.visit[vertex] = self.colors.blue
        self.order.insert(0, vertex)

    def topological_sort(self):
        self.dfs()
        if self.k is None or len(self.order) == 0:
            return None
        else:
            return self.order


def main():
    pass


if __name__ == '__main__':
    main()
