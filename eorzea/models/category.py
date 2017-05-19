from eorzea.extensions import db


class CategoryStatus:
    SHOWN = 0
    HIDDEN = 1


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    order = db.Column(db.Integer, index=True, default=0)
    status = db.Column(db.Integer, default=False, index=True)
    description = db.Column(db.String(100))
