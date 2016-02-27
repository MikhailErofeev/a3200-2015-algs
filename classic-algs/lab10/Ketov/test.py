from lab10 import *

import unittest
class Test (unittest.TestCase):

    def test_main(self):
        array = [23, 247, 19, 96, 264, 265, 132, 181]
        result = findcount(array)
        expected = 2
        self.assertEqual(expected, result)

    def test_empty(self):
        array = []
        result = findcount(array)
        expected = 0
        self.assertEqual(expected, result)




