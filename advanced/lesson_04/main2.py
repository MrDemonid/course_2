from flask import Flask, request
import json
from urllib.parse import unquote_plus

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def _sum():
    array1 = request.form.getlist("a", type=int)
    array2 = request.form.getlist("b", type=int)

    result = ",".join(str(a1+a2) for (a1, a2) in zip(array1, array2))
    return f"Array of sum is [{result}]"




if __name__ == '__main__':
    app.run()
