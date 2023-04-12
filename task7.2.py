import unittest
import random

rndm = []
for i in range(0,10):
    n = random.random()
    rndm.append(n)

class NumTest(unittest.TestCase):
    def test_more_eq(self):
        for n in rndm:
            with self.subTest(i=i):
                self.assertGreaterEqual(n, 0.5)
if __name__ == '__main__':
    unittest.main()


