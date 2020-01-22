#!/usr/bin/python3
"""Script that starts a Flask web application listening on 0.0.0.0:5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
