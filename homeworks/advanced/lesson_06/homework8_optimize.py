import re
from functools import lru_cache


T9_MAPPING = {
    '2': 'abc', '3': 'def', '4': 'ghi',
    '5': 'jkl', '6': 'mno', '7': 'pqrs',
    '8': 'tuv', '9': 'wxyz'
}

WORDS = list()


@lru_cache
def get_t9_pattern(digits: str) -> re.Pattern:
    """
    Создает паттерн из возможных букв на каждую символьную позицию.
    """
    pattern = ''.join(f"[{T9_MAPPING[d]}]" for d in digits)
    return re.compile(f"^{pattern}$", re.IGNORECASE)

def load_words(path='/usr/share/dict/words') -> list[str]:
    with open(path, encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip().isalpha()]


def my_t9(digits: str) -> list[str]:
    pattern = get_t9_pattern(digits)
    length = len(digits)
    return [word for word in WORDS if len(word) == length and pattern.fullmatch(word)]


if __name__ == '__main__':
    print("preload words...")
    WORDS = load_words(path='words.txt')
    print(type(WORDS))
    print("begin T9...")
    words = my_t9("22736368")
    print(words)
    words = my_t9("72779673")
    print(words)
