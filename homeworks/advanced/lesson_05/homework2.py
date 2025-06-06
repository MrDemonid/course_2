import subprocess
import sys

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange

app = Flask(__name__)


class RunCode(FlaskForm):
    code = StringField('code', validators=[InputRequired()])
    timeout = IntegerField('timeout', validators=[DataRequired(), NumberRange(min=1, max=60)])


def run_code(code: str, timeout: int):
    p = None
    try:
        print(f"run code: '{code}'\n")

        # p = subprocess.Popen(["prlimit" "--nproc=1:1", "python", "-c", code],     # для Linux
        p = subprocess.Popen(["python", "-c", code],
                             shell=False,
                             text=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        try:
            _stdout, _stderr = p.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            p.terminate()
            try:
                _stdout, _stderr = p.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                p.kill()
                _stdout, _stderr = p.communicate()
        finally:
            # это на случай, если перенаправлю stdxxx на PIPE.
            if _stdout: print("stdout:", _stdout)
            if _stderr: print("stderr:", _stderr)

        return p.returncode, _stdout, _stderr

    except FileNotFoundError:
        print("Не найден интерпритатор Python!")
    except PermissionError:
        print(f"Нет прав для выполнения: '{code}!")
    except (OSError, ValueError, TypeError) as e:
        print(f"Ошибка выполнения кода: {e}")

    return -1, "", ""


@app.route('/run', methods=['POST'])
def run():
    form = RunCode()
    if form.validate_on_submit():
        ret_code, out, err = run_code(form.code.data, form.timeout.data)
        return (
            f"Return code: {ret_code}\n"
            f"{'-' * 20}\n"
            f"STDOUT:\n{out or ''}\n"
            f"{'-' * 20}\n"
            f"STDERR:\n{err or ''}",
            200
        )
    return f"Invalid parameters: {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
