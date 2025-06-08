import re

T9_MAPPING = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}


def digits_to_regex(digits: str) -> str:
    parts = [f"[{T9_MAPPING[d]}]" for d in digits]
    return ''.join(parts)

def my_t9(digits: str, dict_path='/usr/share/dict/words') -> list[str]:
    pattern = re.compile(f"^{digits_to_regex(digits)}$", re.IGNORECASE)
    with open(dict_path, encoding='utf-8') as f:
        return [line.strip().lower() for line in f if pattern.fullmatch(line.strip())]


if __name__ == '__main__':
    words = my_t9("22736368", 'words.txt')
    print(words)
    words = my_t9("72779673", 'words.txt')
    print(words)