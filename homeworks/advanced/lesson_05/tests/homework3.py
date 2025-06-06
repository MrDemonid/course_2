from homeworks.advanced.lesson_05.homework3 import BlockErrors
import unittest


class TestBlockErrors(unittest.TestCase):

    def test_with_no_division_by_error(self):
        """
        Ошибка игнорируется
        """
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
        except ZeroDivisionError:
            self.fail()

    def test_with_type_error(self):
        """
        Ошибка прокидывается выше.
        """
        with self.assertRaises(TypeError):
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'

    def test_outer_block_no_error(self):
        """
        Ошибка прокидывается выше во внутреннем блоке и игнорируется во внешнем.
        """
        outer_err_types = {TypeError}
        try:
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except:
            self.fail()

    def test_children_ignore_errors(self):
        """
        Дочерние ошибки игнорируются.
        """
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
        except:
            self.fail()
