from files import Files
from slicer import Slicer
from handler import Handler
from dictionary import Dictionary
import os, re


def main(files, slicer, handler, dictionary):

    rawtext = files.read_file()

    raw_list = slicer.slice_to_list(rawtext)

    sliced_sentences = slicer.slice_to_sentences(raw_list)

    handler.crunch_sentences(sliced_sentences)

    done_dict = dictionary.get_all()

    # Test prints..
    print(raw_list[15])
    print(sliced_sentences[15])
    print(done_dict['and'])
    print(done_dict['discuss'])
    print('discuss' in done_dict.keys())

    for key, value in done_dict.items():
        if len(value) > 1:
            print(f"Key: {key},\nvalue: {value}")
    


if __name__ == "__main__":
    # Path to quotes in ./src/data/quote_archive.txt
    quote_archive_path = os.path.join(os.path.expanduser("~"), "Quote_generator", "src", "data", "quote_archive.txt")

    files_object = Files(quote_archive_path)
    
    dictionary_object = Dictionary()

    slicer_object = Slicer()

    handler_object = Handler(dictionary_object, slicer_object)

    

    # Pass file reader and slicer as objects to main-method
    main(files_object, slicer_object, handler_object, dictionary_object)