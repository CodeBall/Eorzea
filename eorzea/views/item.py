import uuid

from flask import abort
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask import request
from flask import render_template
from flask_login import current_user
from flask_login import login_required

from eorzea.forms import ItemForm
from eorzea.forms import ItemCommentForm
from eorzea.forms import ItemTradeForm
from eorzea.services import CategoryService
from eorzea.services import ItemService
from eorzea.services import TradeService
from eorzea.services import UserService
from eorzea.services import ItemCommentService
from eorzea.extensions import qiniu


bp = Blueprint('item', __name__)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    categories = CategoryService.get_categories()
    form = ItemForm()
    if form.add_image.data:
        if len(form.images.entries) < form.images.max_entries:
            form.images.append_entry()
        return render_template('add_item.html', form=form, categories=categories)
    if form.validate_on_submit():
        images = []
        for image in form.images.data:
            filename = f"images/{uuid.uuid4()}.{image.filename.split('.')[-1]}"
            images.append(filename)
            qiniu.upload_stream(image, filename)
        item = ItemService.add_item(title=form.title.data,
                                    description=form.description.data,
                                    images=','.join(images),
                                    location=form.location.data,
                                    category_id=form.category_id,
                                    user_id=current_user.id)
        return redirect(url_for('item.show_item', item_id=item.id))
    return render_template('add_item.html', form=form, categories=categories)


@bp.route('/<int:item_id>', methods=['GET'])
def show_item(item_id):
    categories = CategoryService.get_categories()
    item = ItemService.get_item_by_id(item_id)
    if item is None:
        abort(404)
    item_user = UserService.get_user_by_id(item.user_id)
    if item_user is None:
        abort(404)
    if item.category_id:
        category = CategoryService.get_category_by_id(item.category_id)
    else:
        category = None

    form = ItemCommentForm()
    comments = ItemCommentService.get_comments_by_item_id(item_id)
    for comment in comments:
        if comment.user_id:
            user = UserService.get_user_by_id(comment.user_id)
            if user:
                comment.user = user
    if current_user.id == item.user_id:
        trades = TradeService.get_trades_by_item_id(item_id)
        if trades:
            for tr in trades:
                user = UserService.get_user_by_id(tr.user_id)
                tr.user = user
    else:
        trades=None

    return render_template('item.html', item=item, categories=categories, user=item_user, category=category,
                           comments=comments, comment_form=form, trades=trades)


@bp.route('/<int:item_id>/comment', methods=['POST'])
@login_required
def add_item_comment(item_id):
    item = ItemService.get_item_by_id(item_id)
    if not item:
        abort(404)
    form = ItemCommentForm()

    comment = ItemCommentService.add_comment(content=form.content.data,
                                   user_id=current_user.id,
                                   item_id=item_id)
    if comment:
        flash("评论添加成功!!", "success")
    else:
        flash("额~~发送失败了,请稍后再试~~")

    return redirect(url_for('item.show_item', item_id=item_id))


@bp.route('/<int:item_id>', methods=['POST'])
@login_required
def trade(item_id):
    item = ItemService.get_item_by_id(item_id)
    if not item:
        abort(404)

    if item.user_id == current_user.id:
        flash("不能够申请自己的物品哦~~")
        return redirect(request.referrer)

    item_trade = TradeService.check(current_user.id, item_id)
    if item_trade:
        flash("您已经提交了该物品的交易申请了哦~~")
        return redirect(request.referrer)

    form = ItemTradeForm()
    item_trade = TradeService.add_trade(item_id=item_id,
                                   user_id=current_user.id,
                                   reasion=form.reasion.data,
                                   contact=form.contact.data)
    if item_trade:
        flash("申请交易成功,请耐心等待物品主人主动联系您~~")
    else:
        flash("额~~失败了,请稍后再试")

    return redirect(url_for('item.show_item', item_id=item_id))


@bp.route('/close/<int:item_id>/<int:user_id>')
@login_required
def close(item_id, user_id):
    item = ItemService.get_item_by_id(item_id)
    if not item:
        abort(404)
    trade_user = UserService.get_user_by_id(user_id)
    if not trade_user:
        abort(404)

    item = ItemService.close_item(item_id, user_id)
    if item:
        TradeService.close_trade(item_id)
        flash("结束交易成功")
    else:
        flash("结束交易失败, 请稍后再试")

    return redirect(request.referrer)
