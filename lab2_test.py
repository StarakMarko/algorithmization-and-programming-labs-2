import unittest
from lab_2 import min_distance


class TestCows9(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min_distance([1, 2, 8, 4, 9], 3), 3)


unittest.main()
