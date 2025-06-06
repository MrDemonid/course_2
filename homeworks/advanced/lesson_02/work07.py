from flask import Flask
from datetime import datetime

app = Flask(__name__)

storage = dict()


def str_2_date(src: str):
    if len(src) == 8:
        try:
            return datetime.strptime(src, "%Y%m%d").date()
        except ValueError:
            print(f"Error: value {src} is not date!")
            pass
    return datetime.now().date()


@app.route('/add/<date>/<int:number>')
def add(date, number: int):
    d = str_2_date(date)
    storage.setdefault(d.year, {}).setdefault(d.month, 0)
    storage.setdefault(d.year, {}).setdefault('total', 0)
    storage[d.year][d.month] += number
    storage[d.year]['total'] += number
    print(f"add {d.month}/{d.year} = {storage[d.year][d.month]}\ntotal = {storage[d.year]['total']}")
    return f"Траты за {d.month}/{d.year} в количестве {number} добавлены."


@app.route('/calculate/<int:year>')
def calc_year(year: int):
    if year in storage:
        return f"За {year} год потрачено {storage[year]['total']}"
    return f"За {year} год трат не имеется."


@app.route('/calculate/<int:year>/<int:month>')
def calc_month(year: int, month: int):
    if year in storage and month in storage[year]:
        return f"За {month}/{year} потрачено {storage[year][month]}"
    return f"За {month}/{year} трат не имеется."


if __name__ == '__main__':
    app.run()
