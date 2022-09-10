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


@app.route('/c/<msg>', strict_slashes=False)
def c_msg(msg):
    """Print something"""
    msg = msg.replace('_', ' ')
    return "C {}".format(escape(msg))


@app.route('/python/', strict_slashes=False, defaults={'msg': 'is_cool'})
@app.route('/python/<msg>', strict_slashes=False)
def python_msg(msg="is cool"):
    """Print something"""
    msg = msg.replace('_', ' ')
    return "Python {}".format(escape(msg))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
