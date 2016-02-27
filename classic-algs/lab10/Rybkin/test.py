__author__ = 'Nikita Rybkin'

import unittest
from pythagoras import triples_search

class Test (unittest.TestCase):
    def test_main(self):
        array = [23, 247, 19, 96, 264, 265, 132, 181, 3, 4, 5]
        result = triples_search(array)
        expected = 3
        self.assertEqual(expected, result)

    def test_empty(self):
        array = []
        result = triples_search(array)
        expected = 0
        self.assertEqual(expected, result)
