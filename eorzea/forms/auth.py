from flask_wtf import Form
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from wtforms.fields import StringField
from wtforms.fields import PasswordField
from wtforms.fields import BooleanField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import EqualTo

from eorzea.const import SexMapping
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


class PasswordResetForm(Form):
    email = StringField('Email Address on Account', validators=[DataRequired(),
                                                                Email(),
                                                                Length(max=128)])
    password = PasswordField('New Password', validators=[DataRequired(),
                                                         Length(6, 20),
                                                         EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField(validators=[DataRequired(), Length(6, 20)])

    def validate_email(self, field):
        user = UserService.get_user_by_email(field.data)
        if not user:
            raise ValidationError("The mail without registration")
        else:
            self.user = user


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
    real_name = StringField(validators=[Length(max=128)])
    telephone = StringField(validators=[DataRequired()])
    sex = SelectField(
        choices=[
            (SexMapping.SEX_UNKNOW, "unknow"),
            (SexMapping.SEX_MAN, "man"),
            (SexMapping.SEX_WOMAN, "woman")
        ],
        default="unknow",
        coerce=int
    )
    avatar = FileField("avatar", validators=[FileRequired(),
                                       FileAllowed(['jpg', 'png'], 'Image only!')])

    def validate_email(self, field):
        user = UserService.get_user_by_email(field.data)
        if user:
            raise ValidationError("Email has been used")

    def validate_username(self, field):
        user = UserService.get_user_by_username(field.data)
        if user:
            raise ValidationError("Username has been used")
