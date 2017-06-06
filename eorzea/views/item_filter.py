from flask import Blueprint
from flask import render_template
from flask_login import current_user
from flask_login import login_required

from eorzea.services import ItemService
from eorzea.services import TradeService
from eorzea.services import CategoryService
from eorzea.services import CollectionService


bp = Blueprint('item_filter', __name__)


@bp.route('/category/<int:category_id>')
def item_filter_by_category(category_id):
    categories = CategoryService.get_categories()
    return render_template('index.html', categories=categories)


@bp.route('/active/<int:active>/<int:user_id>')
def item_filter_by_active(active, user_id):
    categories = CategoryService.get_categories()
    return render_template('index.html', categories=categories)


@bp.route('/trade/<int:user_id>')
def item_filter_by_trade(user_id):
    categories = CategoryService.get_categories()
    return render_template('index.html', categories=categories)


@bp.route('/collection')
@login_required
def item_filter_by_collection():
    categories = CategoryService.get_categories()
    return render_template('index.html', categories=categories)
