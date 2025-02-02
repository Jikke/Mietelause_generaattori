from files import Files
from slicer import Slicer
from handler import Handler
from trie import Trie
import os
from ui import UI
import re


def main(files, slicer, handler, ui):
    rawtext = files.read_file()

    ui.start(handler, rawtext)


if __name__ == "__main__":
    # I have been informed that this path does not work. Keeping it as a backup in this comment.
    # quote_archive_path = os.path.join(os.path.expanduser(
    #    "~"), "Quote_generator", "src", "data", "quotes_dataset_one_column_copy.txt")

    # Path to quotes in ./src/data/quotes_dataset_one_column_copy.txt
    quote_archive_path = os.getcwd() + '/src/data/quotes_dataset_one_column_copy.txt'

    files_object = Files(quote_archive_path)

    trie_object = Trie()

    slicer_object = Slicer()

    handler_object = Handler(trie_object, slicer_object)

    ui = UI()

    # Pass file reader and slicer as objects to main-method
    main(files_object, slicer_object, handler_object, ui)
