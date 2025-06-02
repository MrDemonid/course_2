from flask import Flask, request, Response
import subprocess
import shlex

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def ps_command():
    # Получаем список аргументов arg[]=... из URL
    args: list[str] = request.args.getlist('arg')

    # безопасное экранирование всех аргументов
    safe_args = [shlex.quote(arg) for arg in args]

    # формируем полную команду
    cmd = ['ps'] + safe_args

    try:
        # выполняем команду и получаем вывод
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        return Response(
            f"<pre>Command failed:\n{e.stderr or e.stdout}</pre>",
            status=500,
            mimetype='text/html'
        )

    return Response(f"<pre>{output}</pre>", mimetype='text/html')


if __name__ == '__main__':
    app.run(debug=True)

# ps a u x:
# http://localhost:5000/ps?arg=a&arg=u&arg=x
