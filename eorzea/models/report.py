from eorzea.extensions import db


class ReportModel(db.Model):
    __tablename__ = "report"

    id = db.Column(db.Integer, primary_key=True)
    plaintiff_id = db.Column(db.Integer, nullable=False)
    accused_id = db.Column(db.Integer, nullable=False, index=True)
    reasion = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)

    is_valid = db.Column(db.Boolean, nullable=False, default=0)

    valid_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
