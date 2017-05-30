from flask import abort
from flask import Blueprint
from flask import render_template

from eorzea.services import UserService


bp = Blueprint('user', __name__)


@bp.route('/<username>')
def profile(username):
    user = UserService.get_user_by_username(username)
    if not user:
        abort(404)
    return render_template('user/profile.html', user=user)
