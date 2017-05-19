from flask import g
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from flask import Blueprint
from flask_login import login_user

from eorzea.forms import LoginForm
from eorzea.forms import RegisterForm
from eorzea.utils.url import is_safe_url
from eorzea.services import UserService


bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user, form.remember_me.data)
        _next = request.args.get('next')
        if not is_safe_url(_next):
            return abort(400)

        return redirect(_next or url_for('index.index'))
    return render_template('auth/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserService.create_user(form.username.data, form.email.data, form.password.data)
        login_user(user)
        return redirect(url_for('index.index'))
    return render_template('auth/register.html', form=form)
