from flask import Flask
import os

app = Flask(__name__)


# абсолютный путь к директории этого файла (программы)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/head_file/<int:size>/<path:fn>')
def preview(size: int, fn: str):
    abs_path = os.path.abspath(os.path.join(BASE_DIR, fn))
    if os.path.exists(abs_path) and size > 0:
        with open(abs_path, 'r', encoding='utf-8') as f:
            chars = f.read(size)
        res = f"<b>{abs_path}</b> {len(chars)}<br><i>'{chars}'</i>"
        return res
    return f"<h2>Error!</h2><b>{abs_path}</b> not found or never size!"


if __name__ == '__main__':
    print(f"Current: {os.getcwd()}")
    print(f"Base: {BASE_DIR}")
    app.run()
