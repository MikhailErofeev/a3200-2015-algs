import unittest
import triples


class TestPithagoras(unittest.TestCase):

    def test_example_from_exercises(self):
        arr = [23, 247, 19, 96, 264, 265, 132, 181]
        res = triples.find_triples(arr)
        expected = 2
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = triples.find_triples(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_primitive(self):
        arr = [3, 4, 5]
        res = triples.find_triples(arr)
        expected = 1
        self.assertEqual(expected, res)

    def test_without_pythagoras(self):
        arr = [1, 2, 3]
        res = triples.find_triples(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_a_lot_of_triples(self):
        arr = [3, 4, 5, 5, 12, 13, 8, 15, 17, 36, 77, 85, 20, 99, 101, 161, 240, 289]
        res = triples.find_triples(arr)
        expected = 6
        self.assertEqual(expected, res)
