

from abc import abstractmethod
import re

class Slicer:

    def __init__(self):
        return None

    def slice_to_list(self, rawtext):
        """
        Return a list created from slicing rawtext line by line.
        """
        lines = []

        for line in rawtext:
            lines.append(line)

        return lines

    def slice_to_sentences(self, rawlist):
        """
        Return a clean sentence list created from slicing rawlist items.
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
        """
        Return a dictionary with words as keys and words following key word and their amount as nested dictionary. 
        Created from slicing sentence items.
        """

        following_words = {}
        
        current_words = sentence.split()
        current_words = [word.lower() for word in current_words]
        
        prev_word = ""
            
        for word in current_words:

            # New word
            if not word in following_words.keys():

                following_words[word] = {}

            # Current word follows previous word
            if not prev_word == "":

                # Get dictionary of what words follow the previous word
                these_follow = following_words.get(prev_word)

                if word in these_follow:

                    # If this word has already followed previous word, add one to it's dictionary value
                    these_follow[word] += 1

                else:

                    # This word has not previously followed, create dictionary entry
                    these_follow = {word : 1}

                # Update prev_word keys dictionary value
                following_words[prev_word] = these_follow

            # Update prev_word before next iteration 
            prev_word = word
        
        return following_words


        


