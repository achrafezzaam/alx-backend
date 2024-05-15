#!/usr/bin/env python3
''' Create a flask app '''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    ''' Define the Config object '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    ''' Retrieve the locale information '''
    query = request.query_string.decode('utf-8').split('&')
    query_dict = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        query,
    ))
    if 'locale' in query_dict:
        if query_dict['locale'] in app.config["LANGUAGES"]:
            return query_dict['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    ''' Define the index page '''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
