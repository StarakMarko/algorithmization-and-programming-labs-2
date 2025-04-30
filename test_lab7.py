import unittest
from lab7 import build_trie


class TestTrie(unittest.TestCase):
    patterns = ["cat", "car", "cart"]
    trie = build_trie(patterns)

    def test_search(self):
        self.assertTrue(self.trie.search("cat"))

    def test_not_in(self):
        self.assertFalse(self.trie.search("dog"))

    def test_starts_with(self):
        self.assertEqual(self.trie.starts_with("ca"), ["cat", "car", "cart"])


unittest.main()
