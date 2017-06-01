from eorzea.extensions import db


class CollectionModel(db.Model):
    __tablename__ = "collection"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
