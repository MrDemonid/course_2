import subprocess
import shlex
import time


class ManagedProcess:
    def __init__(self, command, *, cwd=None, env=None, shell=False):
        self.command = command
        self.cwd = cwd
        self.env = env
        self.shell = shell
        self.process = None

    def __enter__(self):
        # Преобразование строки в список, если не используется shell
        cmd = self.command if self.shell else shlex.split(self.command)
        print(f"Starting process: {cmd}")
        self.process = subprocess.Popen(
            cmd,
            cwd=self.cwd,
            env=self.env,
            shell=self.shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.process:
            try:
                # Пытаемся дождаться завершения за 10 секунд
                stdout, stderr = self.process.communicate(timeout=10)
            except subprocess.TimeoutExpired:
                print("Timeout. Sending SIGTERM...")
                self.process.terminate()
                try:
                    # Даём еще 5 секунд на мягкое завершение
                    stdout, stderr = self.process.communicate(timeout=5)
                except subprocess.TimeoutExpired:
                    print("Process ignored SIGTERM. Sending SIGKILL...")
                    self.process.kill()  # SIGKILL
                    stdout, stderr = self.process.communicate()
            finally:
                # Этот блок выполнится ВСЕГДА, даже если выше что-то пошло не так
                print(f"Process exited with code {self.process.returncode}")
                if self.process.stdout:
                    print("STDOUT:\n", stdout)
                if self.process.stderr:
                    print("STDERR:\n", stderr)

    def is_running(self):
        return self.process and self.process.poll() is None


if __name__ == "__main__":
    with ManagedProcess("python test_sleep.py") as process:
        while process.is_running():
            print("waiting...")
            time.sleep(1)

    print("Processes stopped.")
