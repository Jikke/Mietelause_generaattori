import unittest
import os
from files import Files
from slicer import Slicer

class TestSclicer(unittest.TestCase):
    def setUp(self):
        self._slicer = Slicer()
        self._files = Files(os.path.join(os.path.expanduser("~"), "Quote_generator", "src", "data", "quote_archive.txt"))
        self._rawtext = self._files.read_file()

    def test_slice_to_raw_lines_works(self):
            lines = self._slicer.slice_to_raw_lines(self._rawtext)

            self.assertEqual(lines[0],'1. "If you want to achieve greatness stop asking for permission." --Anonymous\n')

    def test_slice_specials_works(self):
            lines = self._slicer.slice_to_raw_lines(self._rawtext)
            clean_list = self._slicer.slice_specials(lines)

            self.assertEqual(clean_list[0],'If you want to achieve greatness stop asking for permission.')

    def test_slice_to_word_list_works(self):
            lines = self._slicer.slice_to_raw_lines(self._rawtext)
            clean_list = self._slicer.slice_specials(lines)
            word_list = self._slicer.slice_to_word_list(clean_list[0])

            self.assertEqual(word_list[0],'if')