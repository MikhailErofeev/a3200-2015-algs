class Node:

    def __init__(self, key, left=None, right=None, parent=None):

        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class SplayTree():
    """
    This class includes methods: rotate, split, find, splay, add, merge, remove, contains
      Splay tree description:
        A splay tree is a self-adjusting binary search tree with the additional property that recently accessed elements
        are quick to access again.
        It performs basic operations such as insertion, look-up and removal in O(log n) amortized time.
        For many sequences of non-random operations, splay trees perform better than other search trees, even when the
        specific pattern of the sequence is unknown.
    """

    def __init__(self):
        """Initializing.

         root -- the root of the splay tree
        """

        self.root = None

    def __iter__(self):
        """Iterating the splay tree."""

        v = self.root
        if v is None:
            return
        while True:
            while v.left is not None:
                v = v.left
            k = self.splay(v)
            if k.right is not None:
                v = k.right
                yield k
            else:
                yield k
                break

    @staticmethod
    def set_parent(child, parent):
        """Connects child with his parent.

        child -- linked node
        parent -- node with which child is connecting
        """

        if child is not None:
            child.parent = parent

    def keep_parent(self, v):
        """Connects node with his children.

        v -- value of connecting node
        """

        self.set_parent(v.left, v)
        self.set_parent(v.right, v)

    def rotate(self, parent, child):
        """Swap a node with its parent, keeping all child nodes (and grandparent node) in order.

        parent -- a node on which place child will go
        child -- a node in relation to which rotation is doing
        """

        grandparent = parent.parent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = child
            else:
                grandparent.right = child

        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent

        self.keep_parent(child)
        self.keep_parent(parent)
        child.parent = grandparent

    def splay(self, v):
        """The main function of the splay tree. Moves v in the root by accomplishing zig, zig-zin and zig-zag.

        v -- moving peak
        """

        if v.parent is None:
            return v
        parent = v.parent
        grandparent = parent.parent
        if grandparent is None:
            self.rotate(parent, v)
            return v
        else:
            zigzig = (grandparent.left == parent) == (parent.left == v)
            if zigzig:
                self.rotate(grandparent, parent)
                self.rotate(parent, v)
            else:
                self.rotate(parent, v)
                self.rotate(grandparent, v)
            return self.splay(v)

    def find(self, v, key):
        """Finds if a value is in the tree and moves it to the root of the tree.

        v -- current value
        key -- founded value
        """

        if v is None:
            return None
        if key == v.key:
            return self.splay(v)
        if key < v.key and v.left is not None:
            return self.find(v.left, key)
        if key > v.key and v.right is not None:
            return self.find(v.right, key)
        return self.splay(v)

    def split(self, root, key):
        """Dividing the splay tree in two parts.

        root -- the root of the tree
        key -- value in relation of which we split the tree
        """

        if root is None:
            return None, None
        root = self.find(root, key)
        if root.key == key:
            self.set_parent(root.left, None)
            self.set_parent(root.right, None)
            return root.left, root.right
        if root.key < key:
            right, root.right = root.right, None
            self.set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            self.set_parent(left, None)
            return left, root

    def add(self, key):
        """Adds new node in the splay tree.

        key -- value of added node
        """

        left, right = self.split(self.root, key)
        self.root = Node(key, left, right)
        self.keep_parent(self.root)
        return self.root

    def merge(self, left, right):
        """Connects two trees in one.

        left -- the left tree
        right -- the right tree
        """

        if right is None:
            return left
        if left is None:
            return right
        right = self.find(right, left.key)
        right.left, left.parent = left, right
        return right

    def remove(self, key):
        """Removes given node.

        key -- value of removing node
        """

        root = self.find(self.root, key)
        self.set_parent(root.left, None)
        self.set_parent(root.right, None)
        return self.merge(root.left, root.right)

    def contains(self, key):
        """Determines whether the splay tree contains the key.

        key -- value of checking node
        """

        return self.find(self.root, key) == key
