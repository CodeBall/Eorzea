from datetime import datetime

from eorzea.extensions import db
from eorzea.models import TradeModel


class TradeService:
    @staticmethod
    def add_trade(item_id, user_id, reasion, contact):
        trade = TradeModel(item_id=item_id, user_id=user_id, reasion=reasion, contact=contact)
        db.session.add(trade)
        db.session.commit()

        return trade

    @staticmethod
    def close_trade(item_id):
        trades = TradeService.get_trades_by_item_id(item_id)

        for trade in trades:
            trade.is_closed = True
            trade.closed_at = datetime.now()
            db.session.add(trade)

        db.session.commit()
        return True

    @staticmethod
    def get_trades_by_item_id(item_id):
        trades = TradeModel.query.filter_by(item_id=item_id, is_closed=False)

        return trades

    @staticmethod
    def get_trades_by_user_is(user_id):
        trades = TradeModel.query.filter_by(user_id=user_id, is_closed=False)

        return trades

    @staticmethod
    def check(user_id, item_id):
        return TradeModel.query.filter_by(user_id=user_id, item_id=item_id).first()
