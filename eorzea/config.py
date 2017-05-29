import os

SITE_NAME = 'Eorzea'
ENV_SYMBOL_NAME = 'EORZEA'
APP_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(APP_PATH, '../'))


class BaseConfig:
    DEBUG = True
    SITE_NAME = SITE_NAME
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '\x1d\x00-!\x94\xaf;\x01\x84\x86\xab\x91\x8f\xc3qh\xb6\xcd+\x86\x82\xc4\xf1\xd2')

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://eorzea:eorzea@mysql:3306/eorzea?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # alembic
    ALEMBIC = {
        'script_location': os.path.join(ROOT, 'alembic')
    }

    # qiniu
    QINIU_ACCESS_KEY = os.environ.get('QINIU_ACCESS_KEY', '')
    QINIU_SECRET_KEY = os.environ.get('QINIU_SECRET_KEY', '')
    QINIU_BUCKET_NAME = os.environ.get('QINIU_BUCKET_NAME', 'eorzea')
    QINIU_BASE_URL = os.environ.get('QINIU_BASE_URL', '')


class DevConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


configs = {
    "dev": DevConfig,
    "production": ProductionConfig,
}
