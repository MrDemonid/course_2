rem запуск сервера без app.run()
set FLASK_APP=main1.py
set FLASK_DEBUG=1
python -m flask run --port=5555