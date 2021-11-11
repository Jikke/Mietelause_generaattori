from files import Files
from slicer import Slicer
import os, re


def main(files, slicer):

    rawtext = files_object.read_file()

    raw_list = slicer.slice_to_list(rawtext)

    sliced_sentences = slicer.slice_to_sentences(raw_list)

    words = slicer.slice_to_words(sliced_sentences[15])

    # Test prints..
    print(raw_list[15])
    print(sliced_sentences[15])
    for item in words.items():
        print(item)
    


if __name__ == "__main__":
    # Path to quotes in ./src/data/quote_archive.txt
    quote_archive_path = os.path.join(os.path.expanduser("~"), "Quote_generator", "src", "data", "quote_archive.txt")

    files_object = Files(quote_archive_path)
    
    slicer_object = Slicer()

    # Pass file reader and slicer as objects to main-method
    main(files_object, slicer_object)