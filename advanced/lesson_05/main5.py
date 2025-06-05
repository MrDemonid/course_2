# Контекстный менеджер with. Реализуем свою функцию.

import sys


class SavedFile:
    def __init__(self, path: str, mode='r'):
        self.name = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with SavedFile(sys.argv[1], mode='w') as f:
        f.write('Hello World')
