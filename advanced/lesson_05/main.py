# Запуск и управление процессами

import subprocess


def run_program():
    res = subprocess.run(["python", "test_program_input.py", "-p"], input=b'some input') # , capture_output=True)
    print(res)

if __name__ == "__main__":
    run_program()
