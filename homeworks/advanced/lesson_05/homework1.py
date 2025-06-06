# andrey@andrey-VirtualBox:~$ lsof -i :5000
# COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# python  10954 andrey    5u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
# python  10955 andrey    5u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
# python  10955 andrey    6u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
import os
import signal
import subprocess
import sys
import time

import psutil


def wait_process(pid: int, timeout=5):
    """
    Ожидание остановки процесса.
    """
    start = time.time()
    while time.time() - start < timeout:
        if not psutil.pid_exists(pid):
            return True
        time.sleep(0.1)
    return False


def force_kill(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        if wait_process(pid):
            print(f"Процесс {pid} принудительно завершен!")
        else:
            print(f"Система не может завершить процесс {pid}!")
    except ProcessLookupError:
        print(f"    ❗ Процесс {pid} не существует")
    except PermissionError:
        print(f"    ❗ Недостаточно прав для завершения процесса {pid}")


def kill_process(pid: int):
    print(f"  -- send SIGTERM to pid {pid}")
    try:
        os.kill(pid, signal.SIGTERM)
        time.sleep(5)
        if psutil.pid_exists(pid):
            force_kill(pid)
    except ProcessLookupError:
        print(f"    ❗ Процесс {pid} не существует")
    except PermissionError:
        print(f"    ❗ Недостаточно прав для завершения процесса {pid}")


def true_kill(pid, timeout=5):
    """
    Более удобная и кроссплатформенная версия завершения процесса.
    Жаль в задании сказано использовать os.kill().
    """
    try:
        print(f"  -- send SIGTERM to pid {pid}")
        process = psutil.Process(pid)
        process.terminate()
        process.wait(timeout=5)
        print(f"Процесс {pid} успешно завершен!")
    except psutil.TimeoutExpired:
        print(f"Процесс {pid} не отвечает, отсылаем сигнал SIGKILL.")
        process.kill()
        try:
            process.wait(timeout=3)
            print(f"Процесс {pid} принудительно завершен!")
        except psutil.TimeoutExpired:
            print(f"Critical error! Система не смогла завершить процесс {pid}, перезагрузите компьютер!")
    except psutil.NoSuchProcess:
        print(f"Процесса {pid} не существует! Возможно он уже завершил работу.")


def close_port(port: int):
    """
    Закрывает приложения использующие заданный порт.
    """
    try:
        result = subprocess.run(["lsof", "-i", f":{port}"], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().splitlines()
        if len(lines) < 2:
            print(f"Нет процессов, использующих порт {port}")
            return
        index = next((i for i, h in enumerate(lines[0].split()) if h.lower() == 'pid'), None)
        if index is None:
            print(f"Не удалось найти столбец 'PID' в выводе 'lsof'.")
            return

        pids = set()
        for line in lines[1:]:
            parts = line.split()
            if len(parts) > index and parts[index].isdigit():
                pids.add(int(parts[index]))

        for pid in pids:
            true_kill(pid)          # это лучший вариант.
            # kill_process(pid)     # вариант по заданию.

    except FileNotFoundError:
        print("Не найдена утилита 'lsof'! Убедитесь, что она установлена.")
    except subprocess.CalledProcessError:
        print(f"Нет процессов, использующих порт {port}")


def run_server(path, port):
    close_port(port)
    try:
        p = subprocess.run(['python3', path], stdout=sys.stdout, stdin=sys.stdin, stderr=sys.stderr)
    except KeyboardInterrupt:
        print("Stop process with Ctrl+C")


if __name__ == '__main__':
    run_server("./../../../advanced/lesson_02/main1.py", 5000)
    print('Done!')
