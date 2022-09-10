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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Print something"""
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Print something"""
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Print something"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
