from flask import redirect
from flask import url_for
from flask import request
from flask_login import current_user
from flask_admin import Admin
from flask_admin import AdminIndexView as _AdminIndexView

from eorzea.extensions import db
from eorzea.admin.category import CategoryAdmin


class AdminIndexView(_AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
        # return current_user.is_authenticated and current_user.is_administrator()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))


admin = Admin(
    name='Eorzea Admin',
    index_view=AdminIndexView(name='dashboard', menu_icon_type='fa', menu_icon_value='fa-tachometer'),
)


admin.add_view(CategoryAdmin(db.session, name='category', url='category', menu_icon_type='fa', menu_icon_value='fa-tags'))
