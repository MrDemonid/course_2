# andrey@andrey-VirtualBox:~$ lsof -i :5000
# COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# python  10954 andrey    5u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
# python  10955 andrey    5u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
# python  10955 andrey    6u  IPv4 146998      0t0  TCP localhost:5000 (LISTEN)
import os
import signal
import subprocess




def run_server(path, port: int):
    output = ""
    try:
        result = subprocess.run(["lsof", "-i", f":{port}"], capture_output=True, text=True, check=True)
        output = result.stdout.split("\n")[1:]
    except subprocess.CalledProcessError:
        print(f"Нет процессов, использующих порт {port}")

    pids = set()
    for line in output:
        print("> ", line)
        parts = line.split()
        if len(parts) >= 2:
            pids.add(int(parts[1]))

    for p in pids:
        print(f"  -- send SIGTERM to pid {p}")
        os.kill(p, signal.SIGTERM)



if __name__ == '__main__':
    run_server("", 5000)
