import contextlib


@contextlib.contextmanager
def saved_file(path, mode):
    try:
        f = open(path, mode)
        yield f
    finally:
        f.close()


if __name__ == "__main__":
    with saved_file("test.txt", "w") as f:
        f.write("Hello World\n")
        f.write("Hello Again\n")
