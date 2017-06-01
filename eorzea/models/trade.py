from eorzea.extensions import db


class TradeModel(db.Model):
    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)
    reasion = db.Column(db.String(1024), nullable=False)
    contact = db.Column(db.String(128), nullable=False)

    item_id = db.Column(db.Integer, nullable=False, index=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)

    is_closed = db.Column(db.Boolean, default=False)
    closed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
