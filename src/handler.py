import random

class Handler:
        
    def __init__(self, trie, slicer):
        self._trie = trie
        self._slicer = slicer
    

    def crunch_sentences(self, sentences):
        """
        Create word lists from sentences and add them to trie-datastructure.

        Args:
            sentences (List(String)): Sentences without quotemarks as list.
        """

        for sentence in sentences:
            
            current_words = self._slicer.slice_to_word_list(sentence)
            self._trie.add_sentence(current_words)


    def get_trie(self):
        """
        Get all saved quotes.

        Returns:
            List(String): Quotes from trie-datastructure
        """
        return self._trie.get_all()

    def weight_children(self, node):
        children = node._children
        weighted_words = []
        for word,node in children.items():
            curr_list = [word] * node._occurences
            weighted_words.extend(curr_list)
        return weighted_words


    def create_quote(self, length):
        curr_node = self._trie._root
        quote = []
        for i in range(length):
            weighted_words = self.weight_children(curr_node)
            print(f"weighted_words = {weighted_words}")
            picked_word = random.choice(weighted_words)
            print(f"picked_word = {picked_word}")
            quote.append(picked_word)
            curr_node = curr_node._children[picked_word]
        print(f"quote-list = {quote}")
        return " ".join(quote)


