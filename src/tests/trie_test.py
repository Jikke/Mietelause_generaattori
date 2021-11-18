import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self._trie = Trie()

    def test_instantiating_creates_empty_trie(self):

        self.assertEqual(len(self._trie._root._children), 0)

    def test_adding_new_sentence_works(self):

        sentence = ["Very", "smart", "quote!"]
        self._trie.add_sentence(sentence)

        self.assertEqual(self._trie._root._children["Very"]._word, "Very")

    def test_finding_sentence_works(self):

        sentence = ["Very", "smart", "quote!"]
        self._trie.add_sentence(sentence)

        found = self._trie.does_sentence_exists(["Very", "smart", "quote!"])

        self.assertEqual(found, True)

    def test_get_all_works(self):

        sentence = ["Very", "smart", "quote!"]
        self._trie.add_sentence(sentence)

        all_quotes = self._trie.get_all()

        self.assertEqual(all_quotes, ["Very smart quote!"])
