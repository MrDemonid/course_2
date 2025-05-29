import os.path
from argparse import ArgumentParser
from pathlib import Path


def proceed(base: str, delimiter: str, start_num: int, count: int):
    ends = start_num + count
    print(f"Создаем каталоги '{base}{delimiter}{start_num:>02}' - '{base}{delimiter}{ends:>02}'")

    while count:
        name = f"{base}{delimiter}{start_num:>02}"
        print("-- created ", name)
        Path(name).mkdir(parents=True)
        with open(os.path.join(os.getcwd(), name, 'main.py'), "w", encoding='utf-8') as f:
            f.write(f"# Урок {start_num}")
        start_num += 1
        count -= 1


if __name__ == '__main__':
    p = ArgumentParser(description="Утилита создания группы каталогов.")

    p.add_argument("base", metavar="base-name", type=str, default="lesson",
                   help="Базовое имя создаваемых каталогов, к которому добавляется нумерация.")
    p.add_argument('-d', metavar='symbol', type=str, default=1, help="Разделитель имени и номера урока.")
    p.add_argument("-c", metavar="number", type=int, default=1, help="Начальное значение для нумерации.")
    p.add_argument("-n", metavar="number", type=int, default=1, help="Количество создаваемых каталогов.")

    args = p.parse_args()
    proceed(args.base, args.d, args.c, args.n)
