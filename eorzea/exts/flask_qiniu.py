from urllib.parse import urljoin

from qiniu import Auth
from qiniu import BucketManager
from qiniu import put_data


class Qiniu:
    CONTENT_TYPES = ('image/jpg', 'image/jpeg', 'image/png')

    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.access_key = app.config['QINIU_ACCESS_KEY']
        self.secret_key = app.config['QINIU_SECRET_KEY']
        self.bucket_name = app.config['QINIU_BUCKET_NAME']
        self.base_url = app.config['QINIU_BASE_URL']

        self.q = Auth(self.access_key, self.secret_key)
        self.bucket = BucketManager(self.q)

    def upload_token(self, expires=3600, policy=None):
        return self.q.upload_token(self.bucket_name,
                                   expires=expires,
                                   policy=policy), expires

    def public_url(self, key, suffix=None):
        if not key or key.startswith('http'):
            return key

        if suffix:
            key += suffix
        return urljoin(self.base_url, key)

    def upload_stream(self, file_stream, key, token=None):
        if token is None:
            token = self.upload_token()[0]
        ret, info = put_data(token, key, file_stream)
        if ret is None:
            raise UploadError(info)

    def fetch_url(self, url, key):
        ret, info = self.bucket.fetch(url, self.bucket_name, key)
        if ret is None:
            raise FetchError(info)


class UploadError(Exception):
    pass


class FetchError(Exception):
    pass
