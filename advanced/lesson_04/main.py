# Урок 4 - Flask

from typing import List, Optional, cast
from flask import Flask, request

app = Flask(__name__)


@app.route("/search/", methods=['GET'])
def search():
    # извлекаем аргументы
    cell_tower_ids: list[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"Ypu must specify at least one cell_tower_id", 400

    # извлекаем опциональные параметры
    phone_prefixes: list[str] = request.args.getlist("phone_prefix")
    protocols: list[str] = request.args.getlist("protocol")
    signal_level: Optional[float] = request.args.get("signal_level", type=float)
    # или так:
    # signal_level_raw = request.args.get("signal_level")
    # signal_level: Optional[float] = float(signal_level_raw) if signal_level_raw is not None else None

    return (f"Search for {cell_tower_ids} cell towers. Search criteria: " 
            f"phone_prefixes={phone_prefixes}, " 
            f"protocols={protocols}, " 
            f"signal_level={signal_level}"
            )


@app.route("/test/")
def test():
    d = request.args.to_dict()              # простой словарь, где параметры - это уникальные ключи
    t = request.args.to_dict(flat=False)    # параметры преобразуются в списки (можно с одним ключом передать много значений)
    return f"d = {d}<br>t = {t}"

# http://127.0.0.1:5000/search?cell_tower_id=1&cell_tower_id=2&cell_tower_id=3&phone_prefix=999*&phone_prefix=921*&signal_level=-100



if __name__ == "__main__":
    app.run()
