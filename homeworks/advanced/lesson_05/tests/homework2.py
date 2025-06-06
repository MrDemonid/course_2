import unittest
from homeworks.advanced.lesson_05.homework2 import app


class TestHomework2(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_normal(self):
        data = {
            "code": "import time; print('start test...'); time.sleep(2); print('end test...')",
            "timeout": 15
        }
        response = self.client.post('/run', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("start test...", response.get_data(as_text=True))
        self.assertIn("end test...", response.get_data(as_text=True))

    def test_uncorrected_timeout(self):
        data = {
            "code": "import time; print('start test...'); time.sleep(2); print('end test...')",
            "timeout": '12c'
        }
        response = self.client.post('/run', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("This field is required.", response.get_data(as_text=True))

    def test_uncorrected_code(self):
        data = {
            "code": "import time; printf('start test...')",
            "timeout": 12
        }
        response = self.client.post('/run', data=data)
        self.assertEqual(response.status_code, 200)
        res = response.get_data(as_text=True).split('STDERR')
        self.assertEqual(len(res), 2)
        self.assertIn("Traceback (most recent call last)", res[1])
        self.assertIn("NameError: name 'printf' is not defined.", res[1])



    def test_timeout_expired(self):
        data = {
            "code": "import time; print('start test...'); time.sleep(60); print('end test...')",
            "timeout": 2
        }
        response = self.client.post('/run', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("start test...", response.get_data(as_text=True))
        self.assertNotIn("end test...", response.get_data(as_text=True))

    def test_shell_critical(self):
        data = {
            "code": "import time; print('start test...'); echo hacking!",
            "timeout": 5
        }
        response = self.client.post('/run', data=data)
        self.assertEqual(response.status_code, 200)
        res = response.get_data(as_text=True)
        self.assertIn("start test...", res)
        self.assertNotIn("hacking!", res.split('STDERR')[0])    # в STDERR может содержаться строка с echo hacking!


