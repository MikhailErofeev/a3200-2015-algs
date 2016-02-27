__author__ = 'Dmitry Petrushin'

import unittest

from stacksqueue import *


class TestStacksQueue(unittest.TestCase):
    def test_empty(self):
        queue = MaxElementQueue()
        res = queue.size()
        expected = 0
        self.assertEqual(expected, res)

    def test_trivial(self):
        queue = MaxElementQueue()
        queue.push(3)
        queue.push(1)
        res = queue.max()
        expected = 3
        self.assertEqual(expected, res)

    def test_push(self):
        queue = MaxElementQueue()
        for i in range(1000000):
            queue.push(i)
        res = queue.size()
        expected = 1000000
        self.assertEqual(expected, res)

    ''' It works a long time and eats all ur RAM. Be aware.
    def test_long_push(self):
        queue = MaxElementQueue()
        for i in range(1000000000):
            queue.push(i)
        res = queue.size()
        expected = 1000000000
        self.assertEqual(expected, res)
    '''

    def test_pop(self):
        queue = MaxElementQueue()
        for i in range(1000000):
            queue.push(i)
        for i in range(1000000):
            queue.pop()
        res = queue.size()
        expected = 0
        self.assertEqual(expected, res)

    def test_max_reversed(self):
        queue = MaxElementQueue()
        i = 1000000
        while i >= 0:
            queue.push(i)
            i -= 1
        res = queue.max()
        expected = 1000000
        self.assertEqual(expected, res)

    def test_max_with_pop(self):
        queue = MaxElementQueue()
        for i in range(1000000):
            queue.push(i)
        for i in range(1000000 - 1):
            queue.pop()
        res = queue.max()
        expected = 999999
        self.assertEqual(expected, res)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStacksQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)
