import unittest
from lab_9 import max_word_chain


class TestMaxChain(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_word_chain("a_test.txt"), 5)


unittest.main()
