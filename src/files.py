

class Files:

    def __init__(self, filepath):
        self._path = filepath

    def read_file(self):
        """
        Find file using path given in consturctor.
        Return file as string.
        """
        text = open(self._path, "r")
        return text
