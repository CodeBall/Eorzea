from flask import Flask

from app.extensions import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
