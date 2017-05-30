from flask_login import UserMixin

from eorzea.const import SexMapping
from eorzea.extensions import db
from eorzea.extensions import qiniu


class UserModel(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)
    real_name = db.Column(db.String(128))
    telephone = db.Column(db.String(11), nullable=False)
    sex = db.Column(db.SmallInteger, default=SexMapping.SEX_UNKNOW)
    address = db.Column(db.String(256))
    avatar_url = db.Column(db.String(128))
    active = db.Column(db.Boolean, default=True, nullable=False)  # 账号状态
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            address=self.address,
            avatar_url=qiniu.public_url(self.avatar_url) or '',
        )

    @property
    def is_active(self):
        return self.active
