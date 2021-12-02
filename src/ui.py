from handler import Handler
from trie import Trie
from slicer import Slicer


class UI:  # pragma: no cover

    def __init__(self):
        pass

    def start(self, handler, sliced_sentences):
        key_input = "Empty"
        markov = None
        while(True):
            if markov == None:
                print("\nEmpty input quits program.")
                actual = input(
                    "What level of Markov Chain do you want to use? (1-3): \n")
                try:
                    key_input = int(actual)
                except ValueError:
                    if actual == "":
                        break
                    print("Please input integer only...")
                    continue
                if key_input < 1 or key_input > 3:
                    print("Given Markov level wasn't 1-3.")
                    continue
            markov = key_input
            actual = input(
                "\nHow many words do you want to generate? (4-15): \n")
            try:
                key_input = int(actual)
            except ValueError:
                if actual == "":
                    break
                print("Please input integer only...")
                continue
            if key_input < 4 or key_input > 15:
                print("Given length wasn't 4-15 words.")
                continue
            length = key_input
            handler.crunch_sentences(sliced_sentences, markov)
            quote_list = handler.create_quote(length)
            quote = " ".join(quote_list)
            print(f"\n\"{quote}\"")
