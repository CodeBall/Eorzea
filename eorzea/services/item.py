from eorzea.models import ItemModel
from eorzea.extensions import db


class ItemService:
    @staticmethod
    def get_item_by_id(item_id):
        item = ItemModel.query.get(item_id)
        return item

    @staticmethod
    def add_item(title, description, images, location, user_id):
        item = ItemModel(title=title, description=description, images=images, user_id=user_id)
        db.session.add(item)
        db.session.commit()
        return item
