# Запускаем одним из трех способов.
# 1) Используя конвейер (pipe):
#     ls -l | python3 work02.py
# 2) Тоже конвейер:
#     ls -l > ls.txt
#     cat ls.txt | python3 work02.py
# 3) С использованием перенаправления ввода/вывода:
#     ls - l > ls.txt
#     python3 work02.py < ls.txt

import sys


def get_mean_size(file_list):
    """
    Возвращает средний размер файлов в директории.
    :param file_list: Список строк, полученный по команде ls -l
    """
    total = 0
    count = 0
    for line in file_list:
        try:
            size = int(line.split()[4])
            total += size
            count += 1
        finally:
            pass
    return (total / count) if count > 0 else 0


if __name__ == '__main__':
    # получаем данные с входного потока, за исключением первой строки.
    lines = sys.stdin.readlines()[1:]
    print(f"average size = {get_mean_size(lines):.1f} bytes")
