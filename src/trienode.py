
class Trienode:

    def __init__(self, word):
        """
        _children-dictionary has all the words following this word,
        Key = word as String, Value = corresponding trienode.
        _occurences is the amount this word appears overall (at root), or following this word (2nd level).

        Args:
            word (String): Name of the word to be created as Trienode
        """
        self._word = word
        self._children = {}
        self._occurences = 1
