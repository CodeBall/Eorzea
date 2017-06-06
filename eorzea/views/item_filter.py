from flask import Blueprint
from flask import abort
from flask import render_template
from flask_login import current_user
from flask_login import login_required

from eorzea.services import ItemService
from eorzea.services import TradeService
from eorzea.services import CategoryService
from eorzea.services import CollectionService
from eorzea.services import UserService
from eorzea.services import ItemCommentService


bp = Blueprint('item_filter', __name__)


@bp.route('/category/<int:category_id>')
def item_filter_by_category(category_id):
    categories = CategoryService.get_categories()
    category = CategoryService.get_category_by_id(category_id)
    if not category:
        abort(404)

    items = ItemService.get_items_by_category(category_id)
    items = _format_items(items)

    return render_template('index.html', categories=categories, items=items)


@bp.route('/active/<int:active>/<int:user_id>')
def item_filter_by_active(active, user_id):
    categories = CategoryService.get_categories()
    user = UserService.get_user_by_id(user_id)
    if not user:
        abort(404)

    if active:
        items = ItemService.get_active_items(user_id)
    else:
        items = ItemService.get_success_trade_items(user_id)

    items = _format_items(items)
    return render_template('index.html', categories=categories, items=items)


@bp.route('/trade/<int:user_id>')
def item_filter_by_trade(user_id):
    categories = CategoryService.get_categories()
    user = UserService.get_user_by_id(user_id)
    if not user:
        abort(404)
    trade_item_list = TradeService.get_trades_by_user_is(user_id)
    trade_item_ids = [trade_item.item_id for trade_item in trade_item_list]
    items = ItemService.get_items_by_user_id_list(trade_item_ids)
    items = _format_items(items)
    return render_template('index.html', categories=categories, items=items)


@bp.route('/collection')
@login_required
def item_filter_by_collection():
    categories = CategoryService.get_categories()
    collect_item_list = CollectionService.get_item_list_by_user_id(current_user.id)
    collect_item_ids = [collect_item.item_id for collect_item in collect_item_list]
    items = ItemService.get_items_by_user_id_list(collect_item_ids)
    items = _format_items(items)
    return render_template('index.html', categories=categories, items=items)


def _format_items(items):
    for item in items:
        user = UserService.get_user_by_id(item.user_id)
        if user:
            item.user = user

        if item.category_id:
            category = CategoryService.get_category_by_id(item.category_id)
            if category:
                item.category_name = category.name

        trades = TradeService.get_trades_by_item_id(item.id)
        item.trade_count = len(trades) if trades else 0

        collections = CollectionService.get_user_list_by_item_id(item.id)
        item.collection_count = len(collections) if collections else 0

        comments = ItemCommentService.get_comments_by_item_id(item.id)
        item.comment_count = len(comments) if comments else 0

    return items
