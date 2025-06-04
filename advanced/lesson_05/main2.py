import subprocess


def run_program2():
    p = subprocess.Popen(["python3", "test_sleep.py"], stdout=None, stderr=None)
    return p


if __name__ == '__main__':
    res = run_program2()
    print("done")
    # res.wait()
    res.kill()
    # res.terminate()       # equ Ctrl+C
    # print(res)



