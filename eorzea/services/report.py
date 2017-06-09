from eorzea.models import ReportModel
from eorzea.extensions import db


class ReportService:
    @staticmethod
    def add(plaintiff, accused, reasion, description):
        report = ReportModel(plaintiff_id=plaintiff, accused_id=accused, reasion=reasion, description=description)

        db.session.add(report)
        db.session.commit()

        return report
