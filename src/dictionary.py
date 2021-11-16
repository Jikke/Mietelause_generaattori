
class Dictionary:

    def __init__(self):
        self._following = {}

    def new_word(self, word):
        self._following[word] = {}

    def find(self, word):
        return word in self._following.keys()
    
    def update_following(self, prev_word, word):
        # Get dictionary of what words follow the previous word
        these_follow = self._following.get(prev_word)

        if word in these_follow:
            # If this word has already followed previous word, add one to it's dictionary value
            these_follow[word] += 1

        else:
            # This word has not previously followed, create dictionary entry
            these_follow.update({word : 1})

        # Update prev_word keys dictionary value
        self._following[prev_word] = these_follow

    def get_all(self):
        return self._following
