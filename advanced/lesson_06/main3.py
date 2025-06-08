import csv
import logging
from typing import Optional

from flask import Flask, request
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)



@app.route("/bank/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, 'r', newline='', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f, delimiter=',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
        else:
            return "Person not found", 404


@app.errorhandler(InternalServerError)  # 500
def handle_exception(e: InternalServerError):
    logger.error(f"Handled uncaught exception")
    # Определяем какая именно ошибка произошла
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        logger.error(f"Tried to access {original.filename}. Exception info: {original.strerror}")

    elif isinstance(original, OSError):
        logger.error(f"Unable to access a card. Exception info: {original.strerror}")

    return "Internal server error", 500


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    app.config['WTF_CSRF_ENABLED'] = False
    app.run()
