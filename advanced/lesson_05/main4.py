# Контекстный менеджер и потоки.
import subprocess
import sys

with subprocess.Popen(["python", "test_sleep.py"], stdout=sys.stdout) as p:
    print("hello")

print("Return code", p.returncode, flush=True)

