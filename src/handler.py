
class Handler:
        
    def __init__(self, dictionary, slicer):
        self._dictionary = dictionary
        self._slicer = slicer
    

    def crunch_sentences(self, sentences):

        for sentence in sentences:
            
            current_words = self._slicer.slice_to_words(sentence)
            self.crunch_words(current_words)
            
    def crunch_words(self, words):
        
        prev_word = ""

        for word in words:

            # New word
            if self._dictionary.find(word)==False:
                self._dictionary.new_word(word)

            # Current word follows previous word
            if prev_word != "":
                self._dictionary.update_following(prev_word, word)

            # Update prev_word before next iteration 
            prev_word = word