# Урок 6 - обработка ошибок.

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import FloatField, IntegerField, StringField


app = Flask(__name__)


class Divide(FlaskForm):
    a = FloatField(validators=[InputRequired()])
    b = FloatField(validators=[InputRequired()])


@app.route("/div", methods=['POST'])
def div():
    form = Divide()
    if form.validate_on_submit():
        a = form.a.data
        b = form.b.data
        return f"{a} / {b} = {a/b}", 200

    return f"Bad request. Error: {form.errors}", 400

@app.errorhandler(ZeroDivisionError)
def handle_exception(e: ZeroDivisionError):
    return f"{e.__class__.__name__}: деление на ноль!", 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
