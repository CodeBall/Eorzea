from flask import Blueprint
from flask import render_template

from eorzea.services import CategoryService
from eorzea.services import CollectionService
from eorzea.services import ItemCommentService
from eorzea.services import ItemService
from eorzea.services import TradeService
from eorzea.services import UserService


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    categories = CategoryService.get_categories()
    items = ItemService.get_items(limit=10)

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

    return render_template('index.html', categories=categories, items=items)
