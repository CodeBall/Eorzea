from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from eorzea.models import UserModel
from eorzea.extensions import db


class UserService:
    @staticmethod
    def get_user(username_or_email):
        if '@' in username_or_email:
            user = UserModel.query.filter_by(email=username_or_email).first()
        else:
            user = UserModel.query.filter_by(username=username_or_email).first()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        user = UserModel.query.get(user_id)
        return user

    @staticmethod
    def get_user_by_email(email):
        user = UserModel.query.filter_by(email=email).first()
        return user

    @staticmethod
    def get_user_by_username(username):
        user = UserModel.query.filter_by(username=username).first()
        return user

    @classmethod
    def verify_password(cls, username_or_email, password):
        user = cls.get_user(username_or_email)

        if not user or not check_password_hash(user.password_hash, password):
            return None
        return user

    @staticmethod
    def set_password(uid, password):
        user = UserModel.query.get(uid)
        if not user:
            db.session.commit()
            return
        salted_password = generate_password_hash(password)
        user.password_hash = salted_password
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def create_user(cls, username, email, password, telephone, sex, avatar_url=None, real_name=None):
        user = UserModel(username=username, email=email, telephone=telephone, sex=sex, avatar_url=avatar_url,
                         real_name=real_name)
        db.session.add(user)
        db.session.commit()
        cls.set_password(user.id, password)
        return user
