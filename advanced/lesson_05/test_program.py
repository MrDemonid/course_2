import sys


def main():
    print("Print to STDOUT")
    print("Print to STDERR", file=sys.stderr)


if __name__ == "__main__":
    print("Arguments: ", sys.argv)
    main()
