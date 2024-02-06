#!/usr/bin/env python3
"""this is the flask app module"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config:
    '''the config object instance'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """this is the index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
