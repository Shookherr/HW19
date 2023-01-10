from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns
from views.auths import auth_ns


def create_app(config_object):
    app_ = Flask(__name__)
    app_.config.from_object(config_object)
    register_extensions(app_)
    return app_


def register_extensions(app_):
    db.init_app(app_)
    api = Api(app_)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    # app.run(host="localhost", port=10001, debug=True)
    app.run(host="localhost", port=5000, debug=True)
