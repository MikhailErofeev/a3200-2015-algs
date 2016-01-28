__author__ = 'Nikita Rybkin'


class Set:
    def add(self, item):
        pass

    def remove(self, item):
        pass

    def contains(self, item):
        pass

    def __iter__(self):
        pass


class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None


class SplayTree(Set):
    """
     Uses Splay tree to perform add(), remove() and contains() operations in amortized logarithmic time.
     Short description of the algorithm:
       Splay-tree - a self-balancing binary search tree. The trees do not need to store any additional information,
       which makes it effective for the memory. After each treatment, even search, splay-tree changes its structure.
       The main heuristics splay-tree - move-to-root. After an appeal to any top, it rises to the root. The rise is
       implemented through turns vertices. During one turn, you can swap the parent with the child.
       But simply rotate the top, until it becomes the root, is not enough. Splay-tree trick is that in moving up the
       top of the distance to the root is reduced not only for raising the top, but for all her descendants in the
       current subtree. It uses the technique zig-zig and zig-zag turns.
       The basic idea of zig-zig and zig-zag turns, consider the path from the grandfather to the child. If the path
       is only a left child or only a right, such a situation is called a zig-zig.


    """

    def __init__(self):
        """Creation of an empty tree."""
        self.__root = None

    def __rotate(self, node):
        """Rotation of the edge between node and its parent."""
        parent = node.parent
        node.parent = parent.parent
        if parent.parent is not None:
            if parent.key < parent.parent.key:
                parent.parent.left = node
            else:
                parent.parent.right = node
        parent.parent = node
        if node.key < parent.key:
            parent.left = node.right
            if parent.left is not None:
                parent.left.parent = parent
            node.right = parent
        else:
            parent.right = node.left
            if parent.right is not None:
                parent.right.parent = parent
            node.left = parent
        return node

    def __splay(self, node):
        """Splaying the node."""
        if node.parent is None:
            return node
        if node.parent.parent is None:
            return self.__rotate(node)
        node = self.__rotate(node)
        return self.__splay(self.__rotate(node))

    def __find(self, key):
        """Find a key in the tree and splay it. If there is no such key, return the closest one."""
        current = self.__root
        while current is not None:
            if current.key == key:
                self.__root = self.__splay(current)
                return True, self.__root
            if current.key > key:
                if current.left is None:
                    return False, current
                current = current.left
            else:
                if current.right is None:
                    return False, current
                current = current.right
        return False, current

    def __split(self, key):
        """Splitting the tree into two, left should contain elements less than key, right should contain elements more
        or equals one."""
        result, node = self.__find(key)
        node = self.__splay(node)
        self.__root = node
        if not result:
            if node.key > key:
                left = node.left
                if left is not None:
                    left.parent = None
                node.left = None
                return left, node
            else:
                right = node.right
                if right is not None:
                    right.parent = None
                node.right = None
                return node, right
        else:
            left = node.left
            right = node.right
            if left is not None:
                left.parent = None
            if right is not None:
                right.parent = None
            return left, right

    def __merge(self, left, right):
        """Merging two trees, making the root of the right tree right child of the left tree's max element."""
        if left is None:
            return right
        if right is None:
            return left
        while left.right is not None:
            left = left.right
        left = self.__splay(left)
        left.right = right
        if right is not None:
            right.parent = left
        return left

    def __order_traversal(self, node, queue):
        """Make an ascending order traversal through the tree, adding elements into queue."""
        if node.left is not None:
            self.__order_traversal(node.left, queue)
        queue.append(node.key)
        if node.right is not None:
            self.__order_traversal(node.right, queue)

    def add(self, item):
        """Add element to the set."""
        if self.__root is None:
            self.__root = Node(item, None)
            return
        left, right = self.__split(item)
        self.__root = Node(item, None)
        self.__root.left = left
        self.__root.right = right
        if left is not None:
            left.parent = self.__root
        if right is not None:
            right.parent = self.__root

    def remove(self, item):
        """Remove item from set. If there is no such item, leave set unmodified."""
        result, node = self.__find(item)
        if not result:
            return None
        left = self.__root.left
        right = self.__root.right
        if left is not None:
            left.parent = None
        if right is not None:
            right.parent = None
        self.__root = self.__merge(left, right)
        return item

    def contains(self, item):
        """Check if set contains item."""
        result, node = self.__find(item)
        return result

    def __iter__(self):
        """Iterate through set elements."""
        if self.__root is None:
            return
        queue = []
        self.__order_traversal(self.__root, queue)
        for i in queue:
            yield i