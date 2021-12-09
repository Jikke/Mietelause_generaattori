from handler import Handler
from trie import Trie
from slicer import Slicer
import time



class UI:  # pragma: no cover

    def __init__(self):
        pass

    def start(self, handler, sliced_sentences):
        key_input = "Empty"
        markov = None
        length = None
        starting_words = None
        while(True):
            print("\n--Empty input quits program.--")
            if markov == None:
                actual = input(
                    "What level of Markov Chain do you want to use? (1-3): \n")
                try:
                    key_input = int(actual)
                except ValueError:
                    if actual == "":
                        break
                    print("!Please input integer only!")
                    continue
                if key_input < 1 or key_input > 3:
                    print("!Given Markov level wasn't 1-3!")
                    continue
                markov = key_input
                start_time = time.time()
                handler.crunch_sentences(sliced_sentences, markov)
                print(f"Creating trie took {time.time()-start_time} seconds.")

            if length == None:
                actual = input(
                    "\nHow many words do you want to generate? (4-15): \n")
                try:
                    key_input = int(actual)
                except ValueError:
                    if actual == "":
                        break
                    print("!Please input integer only!")
                    continue
                if key_input < 4 or key_input > 15:
                    print("!Given length wasn't 4-15 words!")
                    continue
                length = key_input

            if starting_words == None:
                actual = input(
                    f"\nGive {markov} lowercase starting words for the quote separated with space (' '): \n")
                try:
                    if actual == "":
                        break
                    key_input = list(actual.split(" "))
                except:
                    print("!Something is wrong with the input!")
                    continue
                if len(key_input) != markov:
                    print(f"!Given amount of words wasn't {markov}!")
                    continue
                starting_words = key_input
            key_input = None

            quote_list = handler.create_quote(starting_words, length)
            if quote_list is not None:
                quote = " ".join(quote_list)
                print(f"\n\"{quote}\"")
            else:
                print("There are no following words for the one(s) given.")

            length = None
            starting_words = None
            quote_list = None
