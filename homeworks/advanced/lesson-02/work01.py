import os


def conv_mem(mem_in_bytes):
    names = ['Bytes', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb']
    count = 0
    used = mem_in_bytes
    while used > 1024:
        used >>= 10
        count += 1
    if count < len(names):
        print(f"cnt = {count} = {(1024**count)}")
        return f"{(mem_in_bytes / (1024**count)):.1f} {names[count]}"
    return f"Used {mem_in_bytes} bytes"


def get_summary_rss(path_to_file):
    """
    Возвращает общее кол-во используемой приложениями и процессами памяти.
    :param path_to_file: файл, полученный из команды ps aux > file.txt
    :return: кол-во используемой памяти в байтах.
    """
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[1:]  # пропускаем первую строку с названиями столбцов

        total = 0
        for line in lines:
            column = int(line.split()[5])
            total += column
        return conv_mem(total)
    return "Unused mem"



if __name__ == '__main__':
    mem = get_summary_rss("/home/andrey/output_file.txt")
    print(mem)
