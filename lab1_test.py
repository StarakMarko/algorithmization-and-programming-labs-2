import unittest
from lab_1 import peak_sequence


class TestFunc(unittest.TestCase):
    def test_sorted_increasing(self):
        increasing_lst = [i for i in range(10)]
        self.assertEqual(peak_sequence(increasing_lst), 0)

    def test_sorted_decreasing(self):
        decreasing_lst = [i for i in range(10, -1)]
        self.assertEqual(peak_sequence(decreasing_lst), 0)

    def test_two_elements(self):
        self.assertEqual(peak_sequence([1, 2]), 0)

    def test_three_peaks(self):
        self.assertEqual(peak_sequence([1, 3, 5, 4, 2, 8, 3, 7, 4]), 5)


unittest.main()
