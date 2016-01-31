import unittest
import Queue

class TestQueue(unittest.TestCase):

    def test_simple(self):
        queue = Queue.StacksQueue()
        queue.push(10)
        queue.push(1)
        queue.push(31)
        res = queue.pop()
        expected = 10
        self.assertEquals(expected, res)

    def test_empty(self):
        queue = Queue.StacksQueue()
        res = queue.pop()
        expected = None
        self.assertEquals(expected, res)

    def test_maximum(self):
        queue = Queue.MaxElementQueue()
        queue.push(10)
        queue.push(111)
        queue.push(1)
        queue.push(12)
        queue.pop()
        queue.pop()
        res = queue.max_elem()
        expected = 12
        self.assertEquals(expected, res)

    def test_MaxElQ_empty(self):
        queue = Queue.MaxElementQueue()
        res = queue.pop()
        expected = None
        self.assertEquals(expected, res)

    def test_full(self):
        queue = Queue.StacksQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.pop()
        queue.pop()
        res1 = queue.pop()
        expected1 = 3
        res2 = queue.pop()
        expected2 = None
        self.assertEquals(expected1, res1)
        self.assertEquals(expected2, res2)

    def test_MaxElQ_negative(self):
        queue = Queue.MaxElementQueue()
        queue.push(-100)
        queue.push(-1)
        queue.push(-1000)
        queue.push(-0.5)
        queue.pop()
        res = queue.max_elem()
        expected = -0.5
        self.assertEquals(expected, res)

    def test_zero_equal(self):
        queue = Queue.MaxElementQueue()
        queue.push(0)
        queue.push(0)
        queue.push(0)
        res = queue.max_elem()
        expected = 0
        self.assertEquals(expected, res)
