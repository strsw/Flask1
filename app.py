from flask import Flask, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return "<p>Привет мир!</p>"

about_me = {
    "name": "Евгений",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru"
}
@app.route("/about")
def about():
    return about_me

quotes_me = [
    {
        "id": 1,
        "author": "Rick Cook",
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 2,
        "author": "Waldi Ravens",
        "text": "Программирование на С похоже на быстрыетанцы на только что отполированном полу людей с острыми бритвами в руках."
    },
    {
        "id": 3,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает.Если бы всё работало, вас бы уволили."
    },
    {
        "id": 4,
        "author": "Yoggi Berra",
        "text": "В теории, теория и практика неразделимы.На практике это не так."
    },
]

@app.route("/quotes")
def quotes():
    return jsonify(quotes_me)


if __name__ == "__main__":
    app.run(debug=True)