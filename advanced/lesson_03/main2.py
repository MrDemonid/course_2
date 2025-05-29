import sys
from datetime import datetime

from flask import Flask


app = Flask(__name__)


MIN_INTEGER = -(sys.maxsize - 1)


# Словарь: номер дня недели -> (род, родительный падеж)
weeks_forms = {
    0: ("м", "понедельника"),
    1: ("м", "вторника"),
    2: ("ж", "среды"),
    3: ("м", "четверга"),
    4: ("ж", "пятницы"),
    5: ("ж", "субботы"),
    6: ("с", "воскресенья"),
}

# Прилагательные в родительном падеже
adj_by_gender = {
    "м": "хорошего",
    "ж": "хорошей",
    "с": "хорошего",
}


def get_good_day(week_day: int):
    """
    Возвращает фразу "Хорошего <день недели>" со склонением.
    :param week_day: День недели (0 - понедельник, 1 - вторник ... 6 - воскресение)
    """
    gender, day_in_genitive = weeks_forms[week_day]
    adj = adj_by_gender[gender]
    return f"{adj.capitalize()} {day_in_genitive}!"


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str):
    """
    Возвращает максимальное число из строки с числами, разделенными символом '/' (path)
    """
    nums = (int(it) for it in numbers.split('/'))
    return f"Максимальное число: <i>{max(nums)}</i>"


@app.route('/hello-world/<string:username>')
def hello(username: str):
    week_day = datetime.today().weekday()
    return f"Привет {username.capitalize()}. {get_good_day(week_day)}"


if __name__ == '__main__':
    app.run()

