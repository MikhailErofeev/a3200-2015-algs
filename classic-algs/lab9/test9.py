import lab9
import unittest
import random
 
class TestKMax(unittest.TestCase):
    def test_random(self):
        a = random.sample(range(100), 50) + random.sample(range(100), 50)
        r1 = lab9.part1(a, 40)
        r2 = lab9.part2(a, 40)
        r = sorted(a)[-40:]
        self.assertEqual(r, sorted(r1))
        self.assertEqual(r, sorted(r2))
    def test_ones(self):
        length = 100000
        k = 10000
        a = [1 for i in range(length)]
        r1 = lab9.part1(a, k)
        r2 = lab9.part2(a, k)
        r = a[-k:]
        self.assertEqual(r, r1)
        self.assertEqual(r, r2)
    def test_long_random(self):
        a = random.sample(range(100000), 20000)
        r1 = lab9.part1(a, 10000)
        r2 = lab9.part2(a, 10000)
        r = sorted(a)[-10000:]
        self.assertEqual(r, sorted(r1))
        self.assertEqual(r, sorted(r2))
 
suite = unittest.TestLoader().loadTestsFromTestCase(TestKMax)
unittest.TextTestRunner(verbosity=2).run(suite)
