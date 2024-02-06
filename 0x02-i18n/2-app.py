#!/usr/bin/env python3
"""this is the flask app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config:
    '''the config object instance'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """this is the get locale method"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """this is the index route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
