#!/usr/bin/env python3
''' Create a flask app '''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    ''' Define the Config object '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    ''' Retrives the user data '''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    ''' Run before any request is resolved '''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    ''' Retrieve the locale information '''
    loc = request.args.get('locale', '')
    if loc in app.config["LANGUAGES"]:
        return loc
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header = request.headers.get('locale', '')
    if header in app.config["LANGUAGES"]:
        return header
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    ''' Define the index page '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
