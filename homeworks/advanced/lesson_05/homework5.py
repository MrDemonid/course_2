import os
import sys


def foo():
    result = 0
    for n in range(1, 11):
        result += n ** 2


def show_file(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    show_file(os.path.abspath(sys.argv[0]))
    foo()
