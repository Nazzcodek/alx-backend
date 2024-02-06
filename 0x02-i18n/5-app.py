#!/usr/bin/env python3
"""this is the flask app module"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__, template_folder='templates')
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''the config object instance'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(user_id):
    """this method get user with their ids"""
    return users.get(user_id)


@app.before_request
def before_request():
    """this method get login user"""
    login_as = request.args.get('login_as')
    if login_as:
        g.user = get_user(int(login_as))
    else:
        g.user = None


@babel.localeselector
def get_locale() -> str:
    """this is the get locale method"""
    args = request.args
    if 'locale' in args and args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/',  methods=['GET'], strict_slashes=False)
def index() -> str:
    """this is the index route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
