from eorzea.admin.mixin import ModelViewMixin
from eorzea.models import UserModel


class UserAdmin(ModelViewMixin):
    can_create = False

    column_exclude_list = ['password_hash']
    column_searchable_list = ['username', 'email']

    def __init__(self, session, **kwargs):
        super(UserAdmin, self).__init__(UserModel, session, **kwargs)
