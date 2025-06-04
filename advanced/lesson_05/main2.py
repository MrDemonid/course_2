import subprocess
import sys
import time


def run_program2():
    p = subprocess.Popen(["python", "test_sleep.py"], stdout=sys.stdout, stderr=None)
    return p


def stop_program2(p: subprocess.Popen):
    print("Stop program: ", p.pid, flush=True)
    p.terminate()
    try:
        p.wait(timeout=5)
        print("Program exited with return code: ", p.returncode, flush=True)
    except subprocess.TimeoutExpired:
        print("Program timed out. Killed!", flush=True)
        p.kill()


if __name__ == '__main__':
    res = run_program2()
    print("done")
    time.sleep(3)
    stop_program2(res)



