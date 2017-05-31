import os

from flask import Flask
from flask_alembic import alembic_click

from eorzea.config import configs
from eorzea.config import ENV_SYMBOL_NAME
from eorzea.config import ROOT
from eorzea.extensions import db
from eorzea.extensions import alembic
from eorzea.extensions import login_manager
from eorzea.extensions import qiniu
from eorzea.views.auth import bp as auth_bp
from eorzea.views.index import bp as index_bp
from eorzea.views.item import bp as item_bp
from eorzea.views.user import bp as user_bp
from eorzea.models import UserModel
from eorzea.admin import admin

LOCAL_CONF = os.path.join(ROOT, 'local_config.py')
SYSTEM_CONF = '/etc/eorzea/conf.py'


def create_app(config=None):
    app = Flask(__name__)
    configure_app(app, config)
    register_extensions(app)
    register_blueprints(app)
    register_command(app)

    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('not_found.html'), 404

    return app


def configure_app(app, config=None):
    # load default configuration
    app.config.from_object(configs[os.environ.get(ENV_SYMBOL_NAME, 'dev')])

    # load system configuration
    if os.path.isfile(SYSTEM_CONF):
        app.config.from_pyfile(SYSTEM_CONF)

    # load local configuration
    if os.path.isfile(LOCAL_CONF):
        app.config.from_pyfile(LOCAL_CONF)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)


def register_extensions(app):
    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    qiniu.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(item_bp, url_prefix='/item')
    app.register_blueprint(user_bp, url_prefix='/user')


def register_command(app):
    app.cli.add_command(alembic_click, 'db')
