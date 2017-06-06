from flask import abort
from flask import Blueprint
from flask import render_template
from flask_login import current_user

from eorzea.services import UserService
from eorzea.services import CategoryService
from eorzea.services import ItemService
from eorzea.services import TradeService
from eorzea.services import CollectionService


bp = Blueprint('user', __name__)


@bp.route('/<username>')
def profile(username):
    user = UserService.get_user_by_username(username)
    if not user:
        abort(404)
    categories = CategoryService.get_categories()
    user = UserService.get_user_by_id(user.id)

    active_items = ItemService.get_active_items(user.id)
    active_item_count = len(active_items) if active_items else 0

    success_trade_items = ItemService.get_success_trade_items(user.id)
    success_trade_count = len(success_trade_items) if success_trade_items else 0

    trade_item_list = TradeService.get_trades_by_user_is(user.id)
    trade_item_count = len(trade_item_list) if trade_item_list else 0

    if current_user.id == user.id:
        collect_item_list = CollectionService.get_item_list_by_user_id(user.id)
        collect_item_count = len(collect_item_list) if collect_item_list else 0
    else:
        collect_item_count = 0

    return render_template('user/profile.html', user=user, categories=categories, active_item_count=active_item_count,
                           success_trade_count=success_trade_count, trade_item_count=trade_item_count,
                           collect_item_count=collect_item_count)
