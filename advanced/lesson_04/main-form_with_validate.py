from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=100000, max=999999)]) # городской номер
    name = StringField(validators=[DataRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField()


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone, name, address = form.email.data, form.phone.data, form.name.data, form.address.data
        print(email, phone, name, address)
        return f"Successfully registered user {email}."

    return f"Invalid input, {form.errors}", 400



if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()

