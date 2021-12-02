import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self._trie = Trie()

    def test_instantiating_creates_empty_trie(self):

        self.assertEqual(len(self._trie._root._children), 0)

    def test_adding_new_sentence_works(self):

        sentence = ["Very", "smart", "quote!"]
        self._trie.add_sentence(sentence, 2)

        self.assertEqual(self._trie._root._children["Very"]._word, "Very")

    def test_adding_occurence_works(self):
        sentence = ["Very", "smart", "quote!"]
        self._trie.add_sentence(sentence, 2)
        sentence = ["Very", "smart", "also!"]
        self._trie.add_sentence(sentence, 2)
        sentence = ["Very", "smart", "too!"]
        self._trie.add_sentence(sentence, 2)

        self.assertEqual(self._trie._root._children["Very"]._occurences, 3)
