__author__ = 'Dmitry Petrushin'
__version__ = '3.4'


class Set:
    def add(self, value):
        pass

    def iterate(self):
        pass


class UnbalancedBinarySearchTree(Set):
    class Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.__root = None
        self.__size = 0

    def __add(self, node, value):
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = self.Node(value)
                node.left.parent = node
            else:
                self.__add(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = self.Node(value)
                node.right.parent = node
            else:
                self.__add(node.right, value)

    def add(self, value):
        if self.__root is None:
            self.__root = self.Node(value)
        else:
            self.__add(self.__root, value)
        self.__size += 1

    def minimum(self, node):
        x = node
        while x.left is not None:
            x = node.left
        return x

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        tmp_node = node.parent
        while tmp_node is not None and node == tmp_node.right:
            node = tmp_node
            tmp_node = tmp_node.parent
        return tmp_node

    def iterate(self):
        if self.__root is not None:
            current = self.minimum(self.__root)
            for _ in range(self.__size):
                yield current.value
                current = self.successor(current)

    def __iter__(self):
        return self.iterate()

    def __len__(self):
        return self.__size
