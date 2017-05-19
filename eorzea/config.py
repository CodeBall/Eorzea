import os

SITE_NAME = 'Eorzea'
ENV_SYMBOL_NAME = 'EORZEA'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(APP_ROOT, '../'))


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '\x1d\x00-!\x94\xaf;\x01\x84\x86\xab\x91\x8f\xc3qh\xb6\xcd+\x86\x82\xc4\xf1\xd2')

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://eorzea:eorzea@mysql:3306/eorzea?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # alembic
    ALEMBIC = {
        'script_location': os.path.join(ROOT, 'alembic')
    }


class DevConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


configs = {
    "dev": DevConfig,
    "production": ProductionConfig,
}

config = configs.get(os.environ.get(ENV_SYMBOL_NAME, 'dev'))
config.SITE_NAME = SITE_NAME
