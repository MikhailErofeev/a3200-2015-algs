import unittest
import splay


class TestSplayTree(unittest.TestCase):

    def test_is_empty(self):
        t = splay.SplayTree()
        self.assertFalse(t.contains(6))

    def test_simple(self):
        t = splay.SplayTree()
        t.add(1)
        t.add(16)
        t.add(96)
        t.add(0)
        t.add(35)
        arr = []
        for v in t:
            arr.append(v.key)
        expected = [0, 1, 16, 35, 96]
        self.assertEquals(expected, arr)

    def test_contains_check(self):
        t = splay.SplayTree()
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in arr:
            t.add(a)
        self.assertFalse(t.contains(10))
        self.assertFalse(t.contains(123456))
