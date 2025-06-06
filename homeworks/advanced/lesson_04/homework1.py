from operator import index

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message='e-mail обязателен'), Email()])
    phone = IntegerField(validators=[DataRequired(message='Номер телефона обязателен'),
                                     NumberRange(min=1000000000, max=9999999999, message='Номер телефона должен состоять из 10 цифр')])
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
