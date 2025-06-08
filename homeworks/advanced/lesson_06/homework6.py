import json

from flask import Flask, Response, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)


@app.route("/div/<int:number>/<int:divider>", methods=["GET"])
def div():
    return "div endpoint"

@app.route("/mul/<int:x>/<int:y>", methods=["GET"])
def mul():
    return "mul endpoint"

@app.route("/set/option", methods=["POST"])
def _set():
    return "set endpoint"


@app.errorhandler(NotFound)
def page_not_found(e: NotFound):
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            routes.append({
                'path': rule.rule,
                'methods': list(rule.methods),
                'endpoint': rule.endpoint
            })
    return jsonify(routes)
    # или стандартным сериализатором:
    # json_str = json.dumps(routes, ensure_ascii=False)
    # return Response(json_str, content_type='application/json; charset=utf-8')




if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
