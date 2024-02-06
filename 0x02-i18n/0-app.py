#!/usr/bin/env python3
"""this is the flask app module"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """this is the index route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
