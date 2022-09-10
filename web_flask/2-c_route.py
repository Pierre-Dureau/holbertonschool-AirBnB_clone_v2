#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print something"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print something"""
    return "HBNB"


@app.route('/c/<message>', strict_slashes=False)
def c_message(message):
    """Print something with a variable"""
    message = message.replace('_', ' ')
    return "C {}".format(escape(message))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
