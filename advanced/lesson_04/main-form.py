from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
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

