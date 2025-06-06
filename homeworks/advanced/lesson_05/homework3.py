class BlockErrors:

    def __init__(self, types: set[type]):
        self.types = types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type is None and issubclass(exc_type, tuple(self.types)):
            return True
        return False


def ex1():
    err_types = {ZeroDivisionError, TypeError}
    with BlockErrors(err_types):
        a = 1 / 0
    print('Выполнено без ошибок')


def ex2():
    err_types = {ZeroDivisionError}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')


def ex3():
    outer_err_types = {TypeError}
    with BlockErrors(outer_err_types):
        inner_err_types = {ZeroDivisionError}
        with BlockErrors(inner_err_types):
            a = 1 / '0'
        print('Внутренний блок: выполнено без ошибок')
    print('Внешний блок: выполнено без ошибок')


def ex4():
    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')


if __name__ == '__main__':
    ex1()       # Выполнено без ошибок
    # ex2()       # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    ex3()       # Внешний блок: выполнено без ошибок
    ex4()       # Выполнено без ошибок
