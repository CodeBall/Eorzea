from eorzea.admin.mixin import ModelViewMixin
from eorzea.models import UserModel


class UserAdmin(ModelViewMixin):
    can_create = False
    can_edit = False
    can_delete = False
    column_display_pk = True

    column_exclude_list = ['password_hash', 'avatar_url']
    column_searchable_list = ['username', 'email']

    column_choices = {
        'sex': (
            (1, '未知'), (2, '男'), (3, '女')
        ),
    }

    column_editable_list = ('real_name', 'telephone', 'address', 'sex', 'is_active')

    def __init__(self, session, **kwargs):
        super(UserAdmin, self).__init__(UserModel, session, **kwargs)
