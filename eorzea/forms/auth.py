from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.fields import PasswordField
from wtforms.fields import BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import EqualTo


from eorzea.services import UserService


class LoginForm(Form):
    username = StringField('Username or email', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

    def validate_password(self, field):
        user = UserService.verify_password(self.username.data, field.data)
        if user is not None:
            self.user = user
        else:
            raise ValidationError('Username or password is invalid')


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),
                                    Email(),
                                    Length(max=128)])
    username = StringField(
        validators=[
            DataRequired(),
            Length(4, 12),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Username must have only letters, '
                   'numbers, dots or underscores')
        ]
    )
    password = PasswordField(validators=[DataRequired(),
                                         Length(6, 20),
                                         EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField(validators=[DataRequired(), Length(6, 20)])

    def validate_email(self, field):
        user = UserService.get_user_by_email(field.data)
        if user:
            raise ValidationError("Email has been used")

    def validate_username(self, field):
        user = UserService.get_user_by_username(field.data)
        if user:
            raise ValidationError("Username has been used")
