import csv
from typing import Optional

from flask import Flask, request
from werkzeug.exceptions import InternalServerError


app = Flask(__name__)


@app.route("/bank/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, 'r') as f:
        csv_reader = csv.DictReader(f, delimiter=',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
        else:
            return "Person not found", 404


@app.errorhandler(InternalServerError)  # 500
def handle_exception(e: InternalServerError):
    # Определяем какая именно ошибка произошла
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        with open("invalid_error.log", "a", encoding="utf-8") as f:
            f.write(f"Tried to access {original.filename}. Exception info: {original.strerror}\n")
    elif isinstance(original, OSError):
        with open("invalid_error.log", "a", encoding="utf-8") as f:
            f.write(f"Unable to access a card. Exception info: {original.strerror}\n")

    return "Internal server error", 500


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
