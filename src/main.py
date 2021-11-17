from files import Files
from slicer import Slicer
from handler import Handler
from trie import Trie
import os, re


def main(files, slicer, handler, trie):

    rawtext = files.read_file()

    raw_lines = slicer.slice_to_raw_lines(rawtext)

    sliced_sentences = slicer.slice_specials(raw_lines)

    handler.crunch_sentences(sliced_sentences)

    done_trie = handler.get_trie()

    # Test prints..
    print(raw_lines[15])
    print(sliced_sentences[15])
    word_list = slicer.slice_to_word_list(sliced_sentences[15])
    print(handler._trie.does_sentence_exists(word_list))
    print("\n".join(done_trie))
    print(f"Items: {len(done_trie)}")
    print(f"Occurences of if: {handler._trie._root._children['if']._occurences}")
    


if __name__ == "__main__":
    # Path to quotes in ./src/data/quote_archive.txt
    quote_archive_path = os.path.join(os.path.expanduser("~"), "Quote_generator", "src", "data", "quote_archive.txt")

    files_object = Files(quote_archive_path)
    
    trie_object = Trie()

    slicer_object = Slicer()

    handler_object = Handler(trie_object, slicer_object)

    

    # Pass file reader and slicer as objects to main-method
    main(files_object, slicer_object, handler_object, trie_object)