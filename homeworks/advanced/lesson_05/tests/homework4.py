# чтобы модуль выполнился самостоятельно (без ключа -m unittest):
# $env: PYTHONPATH = "D:\Users\Andrey\AppData\PyCharmProjects\course_2"
# python .\homeworks\advanced\lesson_05\tests\homework4.py
# иначе if __name__ == '__main__' не сработает, поскольку unittest запускает етсты как модуль,
# а не как самостоятельную программу!

import os

from homeworks.advanced.lesson_05.homework4 import Redirect
import unittest
from io import StringIO


class TestRedirect(unittest.TestCase):

    def test_redirect_stdout(self):
        """
        Проверяем перенаправление STDOUT в наш буфер.
        """
        buffer = StringIO()
        with Redirect(stdout=buffer):
            print("Hello to stdout")
        self.assertIn("Hello to stdout", buffer.getvalue())

    def test_redirect_stderr_with_exception(self):
        """
        Проверяем перенаправление STDERR в наш буфер.
        """
        buffer = StringIO()
        with Redirect(stderr=buffer):
            raise ValueError("Intentional Error")
        result = buffer.getvalue()
        self.assertIn("ValueError", result)
        self.assertIn("Intentional Error", result)

    def test_redirect_both(self):
        """
        Проверка перенаправления в оба буфера сразу.
        """
        out_buffer = StringIO()
        err_buffer = StringIO()
        with Redirect(stdout=out_buffer, stderr=err_buffer):
            print("stdout message")
            raise RuntimeError("stderr message")
        self.assertIn("stdout message", out_buffer.getvalue())
        self.assertIn("RuntimeError", err_buffer.getvalue())

    def test_no_redirect(self):
        """
        Проверка без параметров, просто не должно быть ошибок.
        """
        try:
            with Redirect():
                print("nothing redirected")
        except Exception:
            self.fail("Redirect() raised Exception unexpectedly!")

    def test_invalid_stdout(self):
        """
        Попытка назначить STDOUT неверные данные.
        """
        with self.assertRaises(TypeError):
            Redirect(stdout="not a stream")

    def test_invalid_stderr(self):
        """
        Попытка назначить STDERR неверные данные.
        :return:
        """
        with self.assertRaises(TypeError):
            Redirect(stderr=123)

    def test_nested_redirects(self):
        """
        Проверяем, что при инициализации менеджера сохраняются предыдущие значения sys.stdout и sys.stderr.
        """
        outer_out = StringIO()
        inner_out = StringIO()

        with Redirect(stdout=outer_out):
            print("outer 1")
            # еще раз меняем stdout, менеджер должен сохранить outer_out, в качестве предыдущего значения.
            with Redirect(stdout=inner_out):
                print("inner")
            # менеджер должен был восстановить outer_out
            print("outer 2")

        self.assertEqual(inner_out.getvalue().strip(), "inner")
        self.assertIn("outer 1", outer_out.getvalue())
        self.assertIn("outer 2", outer_out.getvalue())


if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    with open('test_results.txt', 'w', encoding='utf-8') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)
