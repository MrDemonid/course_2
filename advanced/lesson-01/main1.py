"""
Проверка установки Flask: pip freeze | findstr /i flask
Запуск:
a) через app.run()
b) Вручную (не работает):
    1) Создаем переменные окружения:
        setx FLASK_APP main1.py
        setx FLASK_DEBUG 1
    2) Запускаем сервер:
        python -m flask run --port=5555
c) через r.cmd
"""

import datetime
from flask import Flask


app = Flask(__name__)

# endpoint 'test'
@app.route('/test')
def test_function():
    return f"Это тестовая страничка, ответ сгенерирован в {datetime.datetime.now(datetime.UTC)}"


# if __name__ == '__main__':
#     app.run()

