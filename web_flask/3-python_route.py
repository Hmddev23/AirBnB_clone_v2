#!/usr/bin/python3
"""
0. Hello Flask!
start a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    display “Hello HBNB!”
    """
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display “C ” followed by a text variable valaue
    """
    return 'c {}'.format(text.replace("_", " "))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    display “Python ”, followed by a text variable value
    """
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
