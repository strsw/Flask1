from flask import Flask, request, jsonify
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
    return jsonify(about_me)


# Задание 1.1-1.2
@app.route("/quotes/")
@app.route("/quotes/<int:quote_id>")
def get_quote(quote_id=None):
    if quote_id:
        for el in quotes:
            if el["id"] == quote_id:
                return el
        return jsonify({"message": f"Quote with id={quote_id} not found"}), 404
    else:
        return quotes


# Задание 1.3
@app.route("/quotes/count")
def count():
    return jsonify({"count": len(quotes)})


# Задание 1.4
@app.route("/quotes/random")
def rand():
    return quotes[choice(range(len(quotes)))]


# Задание 2.1-2.2
# Доп. задание 2.1
def next_quote_id():
    return quotes[-1]["id"] + 1

def is_valid_rating(rating:int):
    return 1 <= rating <= 5

def set_rating(new_quote):
    try:
        if not is_valid_rating(new_quote["rating"]):
            new_quote["rating"] = 1
    except KeyError:
        new_quote["rating"] = 1
    return new_quote["rating"]


@app.route("/quotes", methods=["POST"])
def create_quote():
    new_quote = request.json
    new_quote["id"] = next_quote_id()
    new_quote["rating"] = set_rating(new_quote)
    quotes.append(new_quote)
    return new_quote, 201


# Задание 2.4
@app.route("/quotes/<int:id>", methods=["PUT"])
def edit_quote(id:int):
    new_quote = request.json
    for quote in quotes:
        if quote["id"] == id:
            for key in new_quote.keys():
                if key in quote.keys():
                    if key == "rating":
                        new_quote[key] = set_rating(new_quote)
                    else:
                        quote[key] = new_quote[key]
            return quote, 200
    return jsonify({"message": "Quote not found"}), 404


# Задание 2.5
@app.route("/quotes/<int:id>", methods=["DELETE"])
def delete(id:int):
    # delete quote with id
    for quote in quotes:
        if quote["id"] == id:
            quotes.remove(quote)
            return jsonify({"message": f"Quote with id {id} is deleted."}), 200
    return jsonify({"message": f"Quote with id {id} not found."}), 404


# Доп. задание 2.2
@app.route("/quotes/filter")
def get_filter():
    args = request.args.to_dict()
    if not args:
        return jsonify({"message": f"filter is empty."}), 404
    result = []
    for quote in quotes:
        found = True
        for key, value in args.items():
            if key in ("id", "rating"):
                value = int(value)
            if quote[key] != value:
                found = False
                break
        if found:
            result.append(quote)
    return result, 200


if __name__ == "__main__":
    app.run(debug=True)