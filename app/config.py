import os

SITE_NAME = 'Eorzea'
ENV_SYMBOL_NAME = 'EORZEA'


class base_config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '\x1d\x00-!\x94\xaf;\x01\x84\x86\xab\x91\x8f\xc3qh\xb6\xcd+\x86\x82\xc4\xf1\xd2')

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/eorzea?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class dev_config(base_config):
    pass


class production_config(base_config):
    pass

configs = {
    "dev": dev_config,
    "production": production_config,
}

config = configs.get(os.environ.get(ENV_SYMBOL_NAME, 'dev'))
config.SITE_NAME = SITE_NAME
