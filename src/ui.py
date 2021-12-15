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
        starting_word = None
        while(True):
            print("\n--Empty input quits program.--")
            if markov == None:
                actual = input(
                    "What level of Markov Chain do you want to use? (1-6): \n")
                try:
                    key_input = int(actual)
                except ValueError:
                    if actual == "":
                        break
                    print("!Please input integer only!")
                    continue
                if key_input < 1 or key_input > 6:
                    print("!Given Markov level wasn't 1-6!")
                    continue
                markov = key_input
                start_time = time.time()
                handler.crunch_sentences(sliced_sentences, markov)
                print(f"Creating trie took {time.time()-start_time} seconds.")

            if length == None:
                actual = input(
                    f"\nHow many words do you want to generate? ({markov+1}-20): \n")
                try:
                    key_input = int(actual)
                except ValueError:
                    if actual == "":
                        break
                    print("!Please input integer only!")
                    continue
                if key_input < markov+1 or key_input > 20:
                    print(f"!Given length wasn't {markov+1}-20 words!")
                    continue
                length = key_input

            if starting_word == None:
                actual = input(
                    f"\nGive lowercase starting word for the quote: \n")
                try:
                    if actual == "":
                        break
                    key_input = actual
                except:
                    print("!Something is wrong with the input!")
                    continue
                if key_input.isalpha():
                    starting_word = key_input
                else:
                    print("!Input had non alphabets!")
                    continue

            word = starting_word
            for i in range(10):  # pylint: disable=unused-variable
                quote_list = handler.create_quote(word, length, markov)
                if quote_list is not None:
                    quote = " ".join(quote_list)
                    print(f"\"{quote}\"")
                    quote = None
                else:
                    print("There are no following words for the one(s) given.")
                quote_list = None

            length = None
            starting_word = None
            
