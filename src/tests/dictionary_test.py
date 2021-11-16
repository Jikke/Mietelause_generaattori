import unittest
from dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()
        self.dictionary.new_word("new")

    def test_instantiating_creates_empty_dictionary(self):

        self.dictionary = Dictionary()

        self.assertEqual(self.dictionary._following, {})

    def test_adding_new_word_works(self):

        found = "new" in self.dictionary._following

        self.assertEqual(found, True)

    def test_finding_word_works(self):

        found = self.dictionary.find("new")

        self.assertEqual(found, True)

    def test_adding_new_following_word_works(self):

        self.dictionary.update_following("new", "i_follow")
        amount = self.dictionary._following.get("new")["i_follow"]

        self.assertEqual(amount, 1)

    def test_updating_following_word_works(self):

        self.dictionary.update_following("new", "i_follow")
        self.dictionary.update_following("new", "i_follow")
        amount = self.dictionary._following.get("new")["i_follow"]

        self.assertEqual(amount, 2)

    def test_get_all_works(self):

        self.dictionary.update_following("new", "i_follow")
        self.dictionary.update_following("new", "i_follow")
        self.dictionary.new_word("added")
        done_dict = self.dictionary.get_all()

        self.assertEqual(done_dict, {'new': {'i_follow': 2}, 'added': {}})