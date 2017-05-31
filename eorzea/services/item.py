from eorzea.models import ItemModel
from eorzea.models import ItemCommentModel
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


class ItemCommentService:
    @staticmethod
    def add_comment(content, item_id, user_id):
        comment = ItemCommentModel(content=content, user_id=user_id, item_id=item_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def get_comments_by_item_id(item_id):
        comments = ItemCommentModel.query.filter(ItemCommentModel.item_id == item_id).all()
        return comments
