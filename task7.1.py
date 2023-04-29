import unittest

def is_num(a):
    if type(a) == int:
        return True
    else:
        return False

def presence(a):
    s = str(a)
    return s

def list1(a):
    l1 = list(a)
    return l1

def list2(b):
    l2 = list(b)
    return l2

class Tests(unittest.TestCase):

    def test_true_false(self):
        self.assertTrue(is_num(23))
        self.assertFalse(is_num('abc'))

    def test_in_notin(self):
        self.assertIn('ab', presence('abc'))
        self.assertNotIn('23', presence('abc'))

    def test_more_less(self):
        a = 23
        b = 45
        self.assertGreater(b,a)
        self.assertLess(a,b)

    def test_equal(self):
        a = '12345'
        b = '54321'
        self.assertCountEqual(list1(a), list2(b))

if __name__ == '__main__':
    unittest.main()