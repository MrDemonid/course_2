import subprocess


def run_program2():
    p = subprocess.Popen(["python", "test_sleep.py"])
    return p


if __name__ == '__main__':
    res = run_program2()
    print("done")
    # print(res)



