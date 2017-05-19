from flask_login import current_user
from flask_admin import Admin
from flask_admin import AdminIndexView as _AdminIndexView

from eorzea.extensions import db
from eorzea.admin.category import CategoryAdmin


class AdminIndexView(_AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
        # return current_user.is_authenticated and current_user.is_administrator()


admin = Admin(
    name='Eorzea Admin',
    index_view=AdminIndexView(name='index'),
)


admin.add_view(CategoryAdmin(db.session, name='category', url='category'))
