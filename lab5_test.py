import unittest
from lab_5 import flood_fill


class TestFloodFill(unittest.TestCase):
    def test_example(self):
        output = [
            ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
            ["Y", "Y", "Y", "Y", "Y", "Y", "G", "C", "C", "C"],
            ["G", "G", "G", "G", "G", "G", "G", "C", "C", "C"],
            ["W", "W", "W", "W", "W", "G", "G", "G", "G", "C"],
            ["W", "R", "R", "R", "R", "R", "G", "C", "C", "C"],
            ["W", "W", "W", "R", "R", "G", "G", "C", "C", "C"],
            ["W", "B", "W", "R", "R", "R", "R", "R", "R", "C"],
            ["W", "B", "B", "B", "B", "R", "R", "C", "C", "C"],
            ["W", "B", "B", "C", "B", "B", "B", "B", "C", "C"],
            ["W", "B", "B", "C", "C", "C", "C", "C", "C", "C"],
        ]
        self.assertEqual(flood_fill("input.txt"), output)


unittest.main()
