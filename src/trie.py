from trienode import Trienode


class Trie:

    def __init__(self):
        """
        _root is "*"-trienode. First words of quotes are it's children.
        _quotes has all quotes as String lists with spaces separating words.
        """
        self._root = Trienode("*")
        self._quotes = []

    def add_sentence(self, sentence):
        """
        Adds new quote to trie-datastructure. First one is handled manually before iterating through them all.
        The trie is in two levels: 
        - the first one is the root level, where all learned words are found as nodes with the word as key
        - the second one has words following their parent node

        Args:
            sentence (List(String)): Clean sliced list of words in quote.
        """

        first_word = sentence.pop(0)

        if first_word not in self._root._children:
            self._root._children[first_word] = Trienode(first_word)
        else:
            self._root._children[first_word]._occurences += 1

        curr_node = self._root._children[first_word]

        for word in sentence:
            if word not in curr_node._children:
                curr_node._children[word] = Trienode(word)
            else:
                curr_node._children[word]._occurences += 1
            # Return to root, add if word is not yet there add it.
            if word not in self._root._children:
                self._root._children[word] = Trienode(word)
            curr_node = self._root._children[word]
        curr_node._is_end_of_sentence = True

    def does_sentence_exists(self, sentence):
        """
        Searches sentence from trie-datastructure.

        Args:
            sentence (List(String)): Sentence to be searched as list.

        Returns:
            Boolean: True when sentence is found.
        """
        if sentence == "":
            return True
        curr_node = self._root
        for word in sentence:
            if word not in curr_node._children:
                return False
            curr_node = self._root._children[word]
        return curr_node._is_end_of_sentence
