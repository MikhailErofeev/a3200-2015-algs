__author__ = 'Nikita Rybkin'

from sys import stdin, stdout
import math

INF = int(2e30)


class SegmentTreeNode:
    def __init__(self, l, r, v=INF):
        self.left = l
        self.right = r
        self.value = v

    def merge(self, left, right):
        if left is not None and right is not None:
            self.value = min(left.value, right.value)
        elif left is None and right is None:
            self.value = INF
        elif left is None:
            self.value = right.value
        else:
            self.value = left.value


class SegmentTree:
    def __init__(self, a):
        n = len(a)
        power = math.ceil(math.log(n, 2))
        total = 2 ** (power + 1)
        self.__tree = [None] * int(total)
        self.__leaf_length = int(total / 2) - 1
        self.__build(1, 0, self.__leaf_length, a)

    def __build(self, node, l, r, a):
        if l == r:
            self.__tree[node] = SegmentTreeNode(l, r)
            try:
                self.__tree[node].value = a[l]
            except IndexError:
                self.__tree[node].value = INF
            return
        left_child = 2 * node
        right_child = left_child + 1
        mid = (l + r) // 2
        self.__build(left_child, l, mid, a)
        self.__build(right_child, mid + 1, r, a)
        self.__tree[node] = SegmentTreeNode(l, r)
        l = self.__tree[left_child]
        r = self.__tree[right_child]
        self.__tree[node].merge(l, r)

    def __query(self, node, l, r, i, j):
        if l >= i and r <= j:
            return self.__tree[node]
        elif j < l or i > r:
            return None
        else:
            left_child = 2 * node
            right_child = left_child + 1
            mid = (l + r) // 2
            l = self.__query(left_child, l, mid, i, j)
            r = self.__query(right_child, mid + 1, r, i, j)
            if l is not None and r is not None:
                return SegmentTreeNode(-1, -1, min(l.value, r.value))
            elif l is None and r is None:
                return SegmentTreeNode(-1, -1, INF)
            elif l is None:
                return SegmentTreeNode(-1, -1, r.value)
            else:
                return SegmentTreeNode(-1, -1, l.value)

    def query(self, i, j):
        return self.__query(1, 0, self.__leaf_length, i, j)

    def __update(self, node, l, r, i, v):
        if l == i and r == i:
            self.__tree[node].value = v
        elif i < l or i > r:
            return None
        else:
            leftchild = 2 * node
            rightchild = leftchild + 1
            mid = (l + r) // 2
            self.__update(leftchild, l, mid, i, v)
            self.__update(rightchild, mid + 1, r, i, v)
            l = self.__tree[leftchild]
            r = self.__tree[rightchild]
            self.__tree[node].merge(l, r)

    def update(self, i, value):
        self.__update(1, 0, self.__leaf_length, i, value)


class Tree:
    def __init__(self, size, adjacent, root):
        self.__size = size
        self.__list = [[] for i in range(size)]
        self.__depths = []
        self.__visited = {}
        for (v1, v2) in adjacent:
            self.__list[v1].append(v2)
            self.__list[v2].append(v1)
        self.__dfs(root)
        self.__st = SegmentTree(self.__depths)

    def least_common_ancestor(self, v1, v2):
        v1 = self.__visited[v1]
        v2 = self.__visited[v2]
        if v1 > v2:
            v1, v2 = v2, v1
        min = self.__st.query(v1, v2)
        return min.value[1]

    def __dfs(self, v, parent=None, depth=0):
        self.__depths.append((depth, v))
        self.__visited[v] = len(self.__depths) - 1
        for child in self.__list[v]:
            if child is not parent:
                self.__dfs(child, v, depth + 1)
                self.__depths.append((depth, v))


if __name__ == "__main__":
    n = int(stdin.readline())
    root = int(stdin.readline())
    adjacent = []
    for i in range(n - 1):
        v1, v2 = stdin.readline().split()
        adjacent.append((int(v1), int(v2)))
    tree = Tree(n, adjacent, root)
    for line in stdin.readlines():
        v1, v2 = line.split()
        stdout.write(str(tree.least_common_ancestor(int(v1), int(v2))) + "\n")