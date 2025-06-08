from flask import Flask
from flask import jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)


registered_routes = []  # сюда будут сохраняться все маршруты


def route(path, methods=None):
    """
    Декоратор для автоматического учета эндпоинтов.
    """
    if methods is None:
        methods = ['GET']

    def decorator(func):
        app.route(path, methods=methods)(func)  # объявляем эндпоинт

        registered_routes.append({
            'path': path,
            'methods': methods,
            'endpoint': func.__name__,
        })
        return func

    return decorator


@route("/div/<int:number>/<int:divider>", methods=["GET"])
def div():
    return "div endpoint"

@route("/mul/<int:x>/<int:y>", methods=["GET"])
def mul():
    return "mul endpoint"

@route("/set/option", methods=["GET", "POST"])
def _set():
    return "set endpoint"


@app.errorhandler(NotFound)
def page_not_found(e: NotFound):
    """
    Обработка исключения 404.
    :return: Список доступных эндпоинтов.
    """
    return jsonify(registered_routes)


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
