"""
С точки зрения логики, было бы достаточно одной проверки с корректными данными.
Ведь если хоть одно поле некорректно, то все тесты test_valid_xxxx() провалятся,
поскольку FlaskForm вернет ошибку в случае ошибки хотя бы в одном поле, независимо
от корректности остальных полей.
Но в задании сказано, сделать для каждого поля, что и сделал.
"""
import unittest
from homework2 import app


def valid_data(**overrides):
    data = {
        'email': 'test@yandex.ru',
        'phone': 9534452805,
        'name': 'John',
        'address': 'Moscow',
        'index': 123456,
        'comment': ''
    }
    data.update(overrides)
    return data


class RegistrationFormTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_valid_email(self):
        data = valid_data()
        response = self.client.post('/registration', data=valid_data())
        expected = f"Successfully registered user {data['email']}"
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.get_data(as_text=True))

    def test_missing_email(self):
        response = self.client.post('/registration', data=valid_data(email="test@yandex,ru"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid email address.", response.get_data(as_text=True))

    def test_missing_email_email_is_none(self):
        response = self.client.post('/registration', data=valid_data(email=""))
        self.assertEqual(response.status_code, 400)
        self.assertIn("e-mail обязателен", response.get_data(as_text=True))


    def test_valid_phone(self):
        data = valid_data()
        response = self.client.post('/registration', data=valid_data())
        expected = f"Successfully registered user"
        expected_phone = f"{data['phone']}"
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.get_data(as_text=True))
        self.assertIn(expected_phone, response.get_data(as_text=True))

    def test_missing_phone(self):
        response = self.client.post('/registration', data=valid_data(phone="369697"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Введите номер сотового телефона.", response.get_data(as_text=True))

    def test_missing_phone_number_of_none(self):
        response = self.client.post('/registration', data=valid_data(phone=""))
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))


    def test_valid_name(self):
        response = self.client.post('/registration', data=valid_data())
        expected = f"Successfully registered user"
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.get_data(as_text=True))

    def test_missing_name(self):
        response = self.client.post('/registration', data=valid_data(name=""))
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))


    def test_valid_address(self):
        response = self.client.post('/registration', data=valid_data())
        expected = f"Successfully registered user"
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.get_data(as_text=True))

    def test_missing_address(self):
        response = self.client.post('/registration', data=valid_data(address=""))
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))


    def test_valid_index(self):
        response = self.client.post('/registration', data=valid_data())
        expected = f"Successfully registered user"
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.get_data(as_text=True))

    def test_missing_index(self):
        response = self.client.post('/registration', data=valid_data(index="124as"))
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))

    def test_missing_index_number_is_none(self):
        response = self.client.post('/registration', data=valid_data(index=""))
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))

