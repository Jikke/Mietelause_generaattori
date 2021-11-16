from dictionary import Dictionary
import re

class Slicer:

    def __init__(self):
        return

    def slice_to_list(self, rawtext):
        """Slices text line by line into list.

        Args:
            rawtext (String): Text read from a .txt file.

        Returns:
            List: Items are lines of the argument.
        """
        lines = []

        for line in rawtext:
            lines.append(line)

        return lines

    def slice_to_sentences(self, rawlist):
        """Removes "-characters from quotes and everything outside of them.

        Args:
            rawlist (List): String list sliced by slice_to_list() -method.

        Returns:
            List: Clean sentence list.
        """
        
        sliced_sentences = []

        for sentence in rawlist:

            edited = sentence

            # Remove characters from beginning before "-char
            edited = re.sub('^[^"]*"', '', edited)

            # Turn string right to left
            turned_edited = edited[::-1]

            # Remove characters from end after "-char
            turned_edited = re.sub('^[^"]*"', '', turned_edited)

            # Turn string back to left to right
            edited = turned_edited[::-1]

            sliced_sentences.append(edited)

        return sliced_sentences



    def slice_to_words(self, sentence):
        
        current_words = sentence.split()
        current_words = [word.lower() for word in current_words]
        
        return current_words





