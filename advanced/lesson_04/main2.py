from flask import Flask, request
import json
from urllib.parse import unquote_plus

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def _sum():
    array1 = request.form.getlist("a", type=int)
    array2 = request.form.getlist("b", type=int)

    result = ",".join(str(a1 + a2) for (a1, a2) in zip(array1, array2))
    return f"Array of sum is [{result}]"


@app.route("/sum2", methods=["POST"])
def _sum2():
    form_data = request.get_data(as_text=True)
    if form_data:
        request_data = unquote_plus(form_data)
        print(f"form_data = {form_data}")
        print(f"request_data = {request_data}")

        arrays = {}
        for encoding_chunk in request_data.split("&"):
            k, v = encoding_chunk.split("=")
            print("  encode: " + k + ", " + v)
            arrays[k] = [int(i) for i in v.split(",")]

        result = ",".join(str(a1 + a2) for (a1, a2) in zip(arrays["a"], arrays["b"]))
        return f"Array of sum is [{result}]"

    return "Ok", 200


@app.route("/sum/json", methods=["POST"])
def _sum_json():
    data = request.get_json()

    print(data)
    array1 = data.get("a", [])      # данные из ключа "a", или []
    array2 = data.get("b", [])      # данные из ключа "b", или []

    result = ",".join(str(a1+a2) for (a1, a2) in zip(array1, array2))
    return f"Array of sum is [{result}]"


@app.route("/sum/json2", methods=["POST"])
def _sum_json2():
    form_data = request.get_data()
    print(form_data)

    data = json.loads(form_data)

    array1 = data.get("a", [])      # данные из ключа "a", или []
    array2 = data.get("b", [])      # данные из ключа "b", или []

    result = ",".join(str(a1+a2) for (a1, a2) in zip(array1, array2))
    return f"Array of sum is [{result}]"




if __name__ == '__main__':
    app.run()
