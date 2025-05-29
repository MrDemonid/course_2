# Тесты для main2.py

import unittest

from advanced.lesson_03.main2 import app


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/max_number/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        """
        Запрос на эндпоинт.
        """
        numbers = 1, 2
        url = self.base_url + '/'.join(str(i) for i in numbers)
        response = self.app.get(url)
        response_text = response.data.decode()
        correct_answer_str = f"<i>{max(numbers)}</i>"
        self.assertTrue(correct_answer_str in response_text)

    def test_can_get_negative_parameters(self):
        params = 1, 2, 's'
        url = self.base_url + '/'.join(str(i) for i in params)
        with self.assertRaises(ValueError):
            self.app.get(url)

