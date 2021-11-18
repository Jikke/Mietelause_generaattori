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
        Adds new quote to trie-datastructure.

        Args:
            sentence (List(String)): Clean sliced list of words in quote.
        """
        curr_node = self._root
        for word in sentence:
            if word not in curr_node._children:
                curr_node._children[word] = Trienode(word)
            else:
                curr_node._children[word]._occurences += 1
            curr_node = curr_node._children[word]
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
            curr_node = curr_node._children[word]
        return curr_node._is_end_of_sentence

    def get(self, node, word_list):
        """ 
        Recursive depth-first search method. 
        When leaf found, adds complete quote to self._quotes.

        Args:
            node (Trienode): Trienode to be handled.
            word_list (List(String)): Words of current path in trie as list.

        Returns:
            [List(String)]: Words of current path in trie as list.
        """
        curr_node = node
        word_list.append(curr_node._word)
        if curr_node._is_end_of_sentence:
            quote = " ".join(word_list)
            self._quotes.append(quote)
            return word_list
        for node in curr_node._children.values():
            self.get(node, word_list)
            del word_list[-1]
        return word_list

    def get_all(self):
        """
        Updates _quotes -list recursively with self.get() -method.

        Returns:
            List(String): Current quotes from trie-datastructure.
        """
        curr_node = self._root
        self._quotes = []
        for node in curr_node._children.values():
            self.get(node, [])
        return self._quotes
