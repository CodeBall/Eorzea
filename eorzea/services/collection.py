from eorzea.extensions import db
from eorzea.models import CollectionModel


class CollectionService:
    @staticmethod
    def add_collection(user_id, item_id):
        collection = CollectionModel(user_id=user_id, item_id=item_id)
        db.session.add(collection)
        db.session.commit()

        return collection

    @staticmethod
    def get_item_list_by_user_id(user_id):
        return CollectionModel.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_list_by_item_id(item_id):
        return CollectionModel.query.filter_by(item_id=item_id).all()

    @staticmethod
    def check_collection(user_id, item_id):
        return CollectionModel.query.filter_by(user_id=user_id, item_id=item_id).first()
