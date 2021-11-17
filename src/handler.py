
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
