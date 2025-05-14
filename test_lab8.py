from lab_8 import ford_fulkerson
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ford_fulkerson("roads.csv"), 15)


unittest.main()
