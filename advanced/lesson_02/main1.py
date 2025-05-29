import os.path

from flask import Flask

app = Flask(__name__)


# передача строки
@app.route('/hello/<username>')         # equ @app.route('/hello/<string:username>')
def hello_function(username):
    return f"Привет {username}!"


# передача целого числа
@app.route("/even/<int:number>")
def even(number: int):
    if number % 2:
        res = "odd"
    else:
        res = "even"
    return f"The number {number:>03} is <b>{res}</b>"

# передача вещественного числа.
# число должно быть с точкой, иначе page not found!
@app.route("/compare/<float:num1>/<float:num2>")
def compare(num1: float, num2: float):
    if num1 < num2:
        res = '<'
    elif num1 > num2:
        res = '>'
    else:
        res = '=='
    return f"<h2>Compare</h2>{num1} {res} {num2}"

# передача строки с возвратом статуса (response)
# проверка: http://127.0.0.1:5000/check/pics/klad-1.png
@app.route("/check/<path:file_path>")
def check(file_path):
    """
    Check if file with relative path exists in file system

    :param file_path: the relative path
    :return: http response
    """
    exists = os.path.exists(file_path)
    res = 'exists' if exists else 'does not exist'
    code = 200 if exists else 404
    return f"File <i>{file_path}</i> {res}", code


if __name__ == '__main__':
    app.run(debug=True)
