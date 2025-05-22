from argparse import ArgumentParser
from pathlib import Path


def proceed(base: str, start_num: int, count: int):
    ends = start_num+count
    print(f"Создаем каталоги '{base}-{start_num:>02}' - '{base}-{ends:>02}'")

    while count:
        name = f"{base}-{start_num:>02}"
        Path(name).mkdir(parents=True)
        start_num += 1
        count -= 1


if __name__ == '__main__':
    p = ArgumentParser(description="Утилита создания группы каталогов.")

    p.add_argument("base", metavar="base-name", type=str, default="lesson", help="Базовое имя создаваемых каталогов, к которому добавляется нумерация.")
    p.add_argument("-c", metavar="number", type=int, default=1, help="Начальное значение для нумерации.")
    p.add_argument("-n", metavar="number", type=int, default=1, help="Количество создаваемых каталогов.")

    args = p.parse_args()
    proceed(args.base, args.c, args.n)

