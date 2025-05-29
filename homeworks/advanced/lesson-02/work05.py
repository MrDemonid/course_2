import sys

from flask import Flask

app = Flask(__name__)


def str_2_int(n):
    try:
        return int(n)
    except ValueError:
        print(f"Warning: value '{n}' is not number!")
        return -(sys.maxsize - 1)


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str):
    nums = (str_2_int(it) for it in numbers.split('/'))
    return f"Максимальное число: <i>{max(nums)}</>"


# # Эталон, но не защищен от ошибок.
# @app.route('/max_number/<path:numbers>')
# def max_number(numbers: str):
#     numbers_as_num = (int(it) for it in numbers.split('/'))
#     return f"Максимальное число: <i>{max(numbers_as_num)}</>"


if __name__ == '__main__':
    app.run()
