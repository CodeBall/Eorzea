from eorzea.extensions import db
from eorzea.extensions import qiniu


class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(512))
    images = db.Column(db.String(1024), default='')
    location = db.Column(db.String(128))

    user_id = db.Column(db.Integer, index=True, nullable=False)
    category_id = db.Column(db.Integer, index=True)
    trade_user_id = db.Column(db.Integer, index=True)

    is_trade = db.Column(db.Boolean, nullable=False, default=0)
    traded_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    @property
    def images_url(self):
        return [qiniu.public_url(image) for image in self.images.split(',')]


class ItemCommentModel(db.Model):
    __tablename__ = 'items_comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    item_id = db.Column(db.Integer, index=True, nullable=False)
    user_id = db.Column(db.Integer, index=True, nullable=False)
