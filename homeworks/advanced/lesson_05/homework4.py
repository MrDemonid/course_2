import sys
import traceback
from io import IOBase


class Redirect:
    def __init__(self, *, stdout: IOBase = None, stderr: IOBase = None):
        if stdout is not None and not isinstance(stdout, IOBase):
            raise TypeError("stdout must be an IOBase-compatible object")
        if stderr is not None and not isinstance(stderr, IOBase):
            raise TypeError("stderr must be an IOBase-compatible object")
        self.new_stdout = stdout
        self.new_stderr = stderr
        self._old_stdout = None
        self._old_stderr = None

    def __enter__(self):
        if self.new_stdout is not None:
            self._old_stdout = sys.stdout
            sys.stdout = self.new_stdout
        if self.new_stderr is not None:
            self._old_stderr = sys.stderr
            sys.stderr = self.new_stderr
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._old_stdout is not None:
            sys.stdout.flush()
            sys.stdout = self._old_stdout
        if self._old_stderr is not None:
            if exc_type:
                sys.stderr.write(traceback.format_exc())
            sys.stderr.flush()
            sys.stderr = self._old_stderr
        return True


if __name__ == '__main__':
    print("Hello stdout")
    stdout_file = open("stdout.txt", "w")
    stderr_file = open("stderr.txt", "w")

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print("Hello stdout.txt")
        raise Exception("Hello stderr.txt")
    stdout_file.close()
    stderr_file.close()

    print("Hello stdout again", flush=True)
    raise Exception("Hello stderr")
