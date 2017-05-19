from flask import Flask
from flask_alembic import alembic_click

from eorzea.extensions import db
from eorzea.extensions import alembic
from eorzea.extensions import login_manager
from eorzea.views.auth import bp as auth_bp
from eorzea.views.index import bp as index_bp
from eorzea.models import UserModel
from eorzea.admin import admin


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_command(app)

    return app


def register_extensions(app):
    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_command(app):
    app.cli.add_command(alembic_click, 'db')
