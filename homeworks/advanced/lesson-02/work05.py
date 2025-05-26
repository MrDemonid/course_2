from flask import Flask


app = Flask(__name__)


def str_2_int(n):
    try:
        return int(n)
    except ValueError:
        print(f"Warning: value '{n}' is not number!")
        return 0


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str):
    nums = numbers.split('/')
    _max = str_2_int(nums[0])
    for n in nums:
        k = str_2_int(n)
        if _max < k:
            _max = k
    return f"Максимальное число: {_max}"


if __name__ == '__main__':
    app.run()

