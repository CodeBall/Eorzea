from flask import redirect
from flask import url_for
from flask import request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView


class ModelViewMixin(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))


class BaseViewMixin(BaseView):

    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))
