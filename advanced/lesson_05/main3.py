# Запуск 5 процессов одновременно.
import os
import time
import subprocess


def run_program():
    start_time = time.time()
    procs = []
    for num in range(1, 6):
        p = subprocess.Popen(["python", "test_sleep.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Process number {} started. PID: {}".format(num, os.getpid()))
        procs.append(p)

    for p in procs:
        p.wait()
        if b'End program' in p.stdout.read() and p.returncode == 0:
            print("Process with PID {} ended successfully".format(p.pid))

    print("Done in {}".format(time.time() - start_time))


if __name__ == '__main__':
    run_program()

