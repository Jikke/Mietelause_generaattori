import unittest
from handler import Handler
from slicer import Slicer
from trie import Trie


class TestHandler(unittest.TestCase):
    def setUp(self):
        trie = Trie()
        sentence = ["so", "very", "smart"]
        trie.add_sentence(sentence, 1)
        sentence = ["very", "smart", "so"]
        trie.add_sentence(sentence, 1)
        sentence = ["smart", "so", "very", ]
        trie.add_sentence(sentence, 1)
        slicer = Slicer()
        self._handler = Handler(trie, slicer)

    def test_weight_children(self):
        weighted_words = self._handler.weight_children(
            self._handler._trie._root)
        self.assertEqual(weighted_words, ['so', 'so', 'so', 'very', 'very', 'very', 'smart', 'smart', 'smart'])

    def test_quote_generation(self):
        quote = self._handler.create_quote(3)
        self.assertEqual(len(quote), 3)
