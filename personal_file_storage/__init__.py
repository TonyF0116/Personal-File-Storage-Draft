from flask import Flask
from .views import account, index
from flask_cors import CORS


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(account.blueprint)
    app.register_blueprint(index.blueprint)

    return app
