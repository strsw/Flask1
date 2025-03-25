from flask import Flask, jsonify
from random import choice

from about import about_me
from quotes import quotes


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hello_world():
    return "<p>Привет мир!</p>"


@app.route("/about")
def about():
    return about_me


# Задание 1-2
@app.route("/quotes/")
@app.route("/quotes/<int:quote_id>")
def get_quote(quote_id=None):
    if quote_id:
        for el in quotes:
            if el["id"] == quote_id:
                return el
        return f"Quote with id={quote_id} not found", 404
    else:
        return quotes


# Задание 3
@app.route("/count")
def count():
    return {"count": len(quotes)}


# Задание 4
@app.route("/rand")
def rand():
    return quotes[choice(range(len(quotes)))]


if __name__ == "__main__":
    app.run(debug=True)