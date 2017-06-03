from flask import Blueprint
from flask import flash
from flask import redirect
from flask import request
from flask import url_for
from flask_login import login_required
from flask_login import current_user

from eorzea.services import CollectionService
from eorzea.services import ItemService


bp = Blueprint('collection', __name__)


@bp.route('/<int:item_id>', methods=['GET'])
@login_required
def add_collection(item_id):

    collection = CollectionService.check_collection(current_user.id, item_id)

    if collection:
        flash("该物品已经收藏过了哦~~")
        return redirect(request.referrer)

    item = ItemService.get_item_by_id(item_id)
    if item and item.user_id == current_user.id:
        flash("不可以收藏自己的物品哦~~")
        return redirect(request.referrer)

    collection = CollectionService.add_collection(current_user.id, item_id)
    if collection:
        flash("收藏成功!", "success")

    return redirect(url_for('index.index'))
