import sys


def main():
    print("Print to STDOUT")
    print("Print to STDERR", file=sys.stderr)
    user_input = input()
    print('User input: "{}"'.format(user_input))


if __name__ == "__main__":
    print("Arguments: ", sys.argv)
    main()
