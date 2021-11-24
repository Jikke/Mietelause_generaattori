import random


class Handler:

    def __init__(self, trie, slicer):
        self._trie = trie
        self._slicer = slicer

    def crunch_sentences(self, sentences):  # pragma: no cover
        """
        Create word lists from sentences and add them to trie-datastructure.

        Args:
            sentences (List(String)): Sentences without quotemarks as list.
        """

        for sentence in sentences:

            current_words = self._slicer.slice_to_word_list(sentence)
            self._trie.add_sentence(current_words)

    def weight_children(self, node):
        """
        Weights children names of the given node.

        Args:
            node (Trienode): Node whose children will be weighted.

        Returns:
            List(String): List of child names multiplied with their occurence-value.
        """
        children = node._children
        weighted_words = []
        for word, node in children.items():
            curr_list = [word] * node._occurences
            weighted_words.extend(curr_list)
        return weighted_words

    def create_quote(self, length):
        """
        Begins at the root of trie,
        weights children along the way and picks words at random,
        iterates according to the number in argument length.

        Args:
            length Integer: How many words will the generated quote have.

        Returns:
            String: Generated quote.
        """
        curr_node = self._trie._root
        quote = []
        for i in range(length):  # pylint: disable=unused-variable
            weighted_words = self.weight_children(curr_node)
            picked_word = random.choice(weighted_words)
            # Has following words.
            if len(self._trie._root._children[picked_word]._children) > 0:
                quote.append(picked_word)
                curr_node = self._trie._root._children[picked_word]
            # Has not following words. End sentence and start from root.
            else:
                picked_word = picked_word + "."
                quote.append(picked_word)
                curr_node = self._trie._root

        quote[0] = quote[0].capitalize()
        return " ".join(quote)
