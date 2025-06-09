import unittest
from homeworks.advanced.lesson_06.homework8_T9Trie import T9Trie


class TestT9Trie(unittest.TestCase):
    def setUp(self):
        """
        Подготавливаем словарь для тестов.
        """
        self.words = ["cat", "bat", "bar", "basement", "cab", "password", "passwords"]
        self.trie = T9Trie(self.words)

    def test_word_to_digits(self):
        """
        Проверяем корректность преобразования слова в числовой код.
        """
        self.assertEqual(self.trie._word_to_digits("cat"), "228")
        self.assertEqual(self.trie._word_to_digits("bat"), "228")
        self.assertEqual(self.trie._word_to_digits("bar"), "227")
        self.assertEqual(self.trie._word_to_digits("basement"), "22736368")

    def test_search_exact(self):
        self.assertCountEqual(self.trie.search_exact("227"), ["bar"])
        self.assertCountEqual(self.trie.search_exact("228"), ["cat", "bat"])
        self.assertCountEqual(self.trie.search_exact("22736368"), ["basement"])
        self.assertEqual(self.trie.search_exact(""), [])
        self.assertEqual(self.trie.search_exact("999999999"), [])

    def test_search_prefix(self):
        self.assertCountEqual(self.trie.search_prefix("227"), ["bar", "basement"])
        self.assertCountEqual(self.trie.search_prefix("72779673"), ["password", "passwords"])
        self.assertCountEqual(self.trie.search_prefix(""), self.words)
        self.assertEqual(self.trie.search_prefix("999999999"), [])

    def test_invalid_chars(self):
        """
        Символы вне алфавита отсеиваются. Проверим это.
        """
        self.assertEqual(self.trie._word_to_digits("pa$$word"), "729673")   ## $$ не пройдут


if __name__ == '__main__':
    unittest.main()

