from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_login import LoginManager

from eorzea.exts.flask_qiniu import Qiniu

db = SQLAlchemy()
alembic = Alembic()
login_manager = LoginManager()
qiniu = Qiniu()


login_manager.login_view = 'auth.login'
