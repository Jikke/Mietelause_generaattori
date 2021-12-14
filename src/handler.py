import random


class Handler:

    def __init__(self, trie, slicer):
        self._trie = trie
        self._slicer = slicer

    def crunch_sentences(self, sentences, level):  # pragma: no cover
        """
        Create word lists from sentences and add them to trie-datastructure.

        Args:
            sentences (List(String)): Sentences without quotemarks as list.
        """

        for sentence in sentences:

            current_words = self._slicer.slice_to_word_list(sentence)
            self._trie.add_sentence(current_words, level)

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
        for word, trie_node in children.items():
            curr_list = [word] * trie_node._occurences
            weighted_words.extend(curr_list)
        return weighted_words

    def get_leaf(self, words):
        """
        Gets words as argument of which following word is picked at random 
        (propabilities are influenced by word's occurence after these specific words).

        Args:
            words List(String): List of words previous to the to be picked one.

        Returns:
            String: Name of picked word.
        """
        curr_node = self._trie._root
        for i in range(len(words)+1):
            if i == len(words):
                picked_word = self.get_random_child(curr_node)
                return picked_word
            if words[i] in curr_node._children:
                curr_node = curr_node._children[words[i]]
                continue
            return None

    def get_random_child(self, node):
        """
        Weights and picks random child of the node given as argument.

        Args:
            node (Trienode): Parent trienode of whose children will be picked.

        Returns:
            String: Random name of children picked.
        """
        if len(node._children) > 0 and node._children is not None:
            weighted_words = self.weight_children(node)
            return random.choice(weighted_words)
        return None

    def create_quote(self, starting_words, length):
        """
        Begins at the root of trie,
        weights children along the way and picks words at random,
        iterates according to the number in argument length.

        Args:
            starting_words List(String): Words with which the generated quote begins.
            length Integer: How many words will the generated quote have.

        Returns:
            List(String): Generated quote as list.
        """

        quote = starting_words
        first_generated_word = self.get_leaf(starting_words)
        if first_generated_word is not None:
            quote.append(first_generated_word)
        else:
            return None
        current_words = starting_words[1:]

        for i in range(length-len(quote)):  # pylint: disable=unused-variable
            picked_word = self.get_leaf(current_words)
            if picked_word is not None:
                quote.append(picked_word)
                current_words.pop(0)
                current_words.append(picked_word)
            else:
                print("No more following words found.")
                break

        quote[0] = quote[0].capitalize()
        quote[-1] = quote[-1]+"."
        return quote
