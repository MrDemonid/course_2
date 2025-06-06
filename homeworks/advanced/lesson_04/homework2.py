from operator import index
from typing import Optional

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange, ValidationError

app = Flask(__name__)


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        """
        Валидатор длины номера телефона (сотового) в виде функции.
        """
        l = len(str(field.data))
        if l < min or l > max:
            msg = f"Number must be range from {min} to {max}" if message is None else message
            raise ValidationError(msg)

    return _number_length


class NumberLength:
    """
    Валидатор длины номера телефона (сотового) в виде класса.
    """
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self._min = min
        self._max = max
        self._message = message or f"Number must be in range from {min} to {max}"

    def __call__(self, form: FlaskForm, field: Field):
        length = len(str(field.data))
        if length < self._min or length > self._max:
            raise ValidationError(self._message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message='e-mail обязателен'), Email()])
    # phone = IntegerField(validators=[DataRequired(), number_length(10, 10)])
    phone = IntegerField(validators=[DataRequired(), NumberLength(10, 10, message="Введите номер сотового телефона.")])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[DataRequired()])
    comment = StringField()


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone, name, address = form.email.data, form.phone.data, form.name.data, form.address.data
        idx, comment = form.index.data, form.comment.data
        print(email, phone, name, address, idx, comment)
        return f"Successfully registered user {email} with phone +7{phone}."

    return f"Invalid input, {form.errors}", 400



if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
