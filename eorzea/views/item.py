import uuid

from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import render_template
from flask_login import current_user
from flask_login import login_required

from eorzea.forms import ItemForm
from eorzea.services import ItemService
from eorzea.extensions import qiniu


bp = Blueprint('item', __name__)


@bp.route('/', methods=['GET', 'POST'])
@login_required
def add_item():
    form = ItemForm()
    if form.add_image.data:
        if len(form.images.entries) < form.images.max_entries:
            form.images.append_entry()
        return render_template('item.html', form=form)
    if form.validate_on_submit():
        images = []
        for image in form.images.data:
            filename = 'images/{}.{}'.format(uuid.uuid4(), image.filename.split('.')[-1])
            images.append(filename)
            qiniu.upload_stream(image, filename)
        ItemService.add_item(title=form.title.data,
                             description=form.description.data,
                             images=','.join(images),
                             location=form.location.data,
                             user_id=current_user.id)
        return redirect(url_for('index.index'))
    return render_template('item.html', form=form)
