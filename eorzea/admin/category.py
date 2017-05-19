from eorzea.admin.mixin import ModelViewMixin
from eorzea.models import CategoryModel


class CategoryAdmin(ModelViewMixin):
    def __init__(self, session, **kwargs):
        super(CategoryAdmin, self).__init__(CategoryModel, session, **kwargs)
