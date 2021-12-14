from trienode import Trienode


class Trie:

    def __init__(self):
        """
        _root is "*"-trienode.
        """
        self._root = Trienode("*")

    def add_sentence(self, sentence, level):
        """
        Adds words into trie-datastructure according to the used level of Markov chain.
        This method handles sentences into shorter word-lists, actual storing happens in add_words -method.

        Args:
            sentence (List(String)): Clean sliced list of words in quote.
        """
        level += 1
        for i in range(len(sentence)):  # pylint: disable=unused-variable
            slice_len = len(sentence) - level
            # If more words left in sentence than level+1
            if slice_len > 0:
                sliced_sentence = sentence[:-slice_len]
            # Else just dump rest of words to trie
            else:
                sliced_sentence = sentence
            self.add_words(sliced_sentence)
            sentence.pop(0)

    def add_words(self, words):
        """
        Adds words into trie-datastructure according to the length of words-list.

        Args:
            words List(String): Length of this list depends on the level of Markov chain.
        """
        curr_node = self._root
        for i in range(len(words)):
            if words[i] in curr_node._children:
                curr_node._children[words[i]]._occurences += 1
            else:
                curr_node._children[words[i]] = Trienode(words[i])
            curr_node = curr_node._children[words[i]]
