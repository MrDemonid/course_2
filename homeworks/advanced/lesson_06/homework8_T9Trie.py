# T9 с подбором слов через дерево. Самый быстрый вариант - O(1)
# Можно еще быстрее, храня в узлах не индексы слов, а сами слова,
# но это раздувает расход памяти в 5-7 раз (от размера исходного словаря),
# поэтому хранение индексов видится неплохим компромиссом между скоростью и небольшой
# экономией памяти.


def load_words(path='/usr/share/dict/words') -> list[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip().isalpha()]


class T9TrieNode:
    def __init__(self):
        self.children = {}
        self.word_indices = []
        self.terminal_indices = []  # сюда складываем слова, которые "заканчиваются" на этой цифре

class T9Trie:
    def __init__(self, dictionary):
        self.root = T9TrieNode()
        self.words = dictionary  # общий список слов
        self.t9_map = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        self.char_to_digit = {ch: digit for digit, letters in self.t9_map.items() for ch in letters}
        self._build_trie()

    def _word_to_digits(self, word: str) -> str:
        return ''.join(self.char_to_digit.get(ch, '') for ch in word.lower())

    def _build_trie(self):
        """
        Подготовка дерева.
        """
        for idx, word in enumerate(self.words):
            dig = self._word_to_digits(word)
            if not dig:
                continue
            node = self.root
            node.word_indices.append(idx)
            for digit in dig:
                if digit not in node.children:
                    node.children[digit] = T9TrieNode()
                node = node.children[digit]
                node.word_indices.append(idx)
            node.terminal_indices.append(idx)   # точное соответствие

    def search_exact(self, digits: str) -> list[str]:
        """
        Для поиска точных совпадений.
        """
        node = self.root
        for digit in digits:
            if digit not in node.children:
                return []
            node = node.children[digit]
        return [self.words[i] for i in node.terminal_indices]

    def search_prefix(self, digits: str) -> list[str]:
        """
        Для автодополнения (все, что начинается с префикса)
        """
        node = self.root
        for digit in digits:
            if digit not in node.children:
                return []
            node = node.children[digit]
        return [self.words[i] for i in node.word_indices]



if __name__ == "__main__":
    words = load_words(path='words.txt')
    trie = T9Trie(words)

    while True:
        digits = input("Enter digits (2–9): ")
        if not digits:
            break
        print("Matches:", trie.search_exact(digits))
        print("Matches:", trie.search_prefix(digits))
