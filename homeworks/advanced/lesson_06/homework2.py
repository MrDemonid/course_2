import re
import bisect


class WordList:
    """
    Создает отсортированный список английских слов,
    для быстрого бинарного поиска (O(log N))
    Чтобы не изобретать велосипед, для поиска используется
    библиотечный модуль bisect.
    """
    def __init__(self, path='/usr/share/dict/words', min_len=5):
        with open(path, encoding='utf-8') as f:
            self.words = sorted(
                line.strip().lower()
                for line in f
                if len(line.strip()) >= min_len and line[0].isalpha()
            )
            print(f"found {len(self.words)} words")

    def contains(self, word: str) -> bool:
        word = word.lower()
        index = bisect.bisect_left(self.words, word)
        return index < len(self.words) and self.words[index] == word


def extract_words_from_password(password: str, min_len=5):
    """
    Разбивает пароль на слова. Критерий разбивки простой - в качестве
    разделителя служат любые не буквенные символы.
    """
    return [
        word.lower()
        for word in re.split(r'[^a-zA-Z]+', password)
        if len(word) >= min_len
    ]


def is_strong_password(password: str, dictionary: WordList) -> bool:
    """
    Собственно проверка пароля.
    """
    words = extract_words_from_password(password)
    return not any(dictionary.contains(word) for word in words)


if __name__ == '__main__':
    words = WordList('words.txt')
    print(is_strong_password("MySecure.Password123!@#", words))
