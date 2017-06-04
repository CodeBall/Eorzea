from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from wtforms.fields import StringField
from wtforms.fields import TextAreaField
from wtforms.fields import SubmitField
from wtforms.fields import SelectField
from wtforms.fields import FieldList
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Length

from eorzea.services import CategoryService


class ItemForm(Form):
    title = StringField(validators=[DataRequired(), Length(max=20)])
    description = TextAreaField(validators=[DataRequired(), Length(max=512)])
    images = FieldList(
        FileField('image', validators=[FileRequired(),
                                       FileAllowed(['jpg', 'png'], 'Image only!')]),
        validators=[DataRequired()],
        min_entries=1, max_entries=3)
    location = StringField(validators=[DataRequired(), Length(max=128)])
    category = SelectField()
    add_image = SubmitField()

    def __init__(self):
        super(ItemForm, self).__init__()
        self.category.choices = CategoryService.get_category_choices()

    def validate_category(self, field):
        category = CategoryService.get_category_by_slug(field.data)
        if not category:
            raise ValidationError('invalid category')
        self.category_id = category.id


class ItemCommentForm(Form):
    content = TextAreaField(validators=[DataRequired(), Length(max=512)])


class ItemTradeForm(Form):
    contact = StringField(validators=[DataRequired(), Length(min=11, max=11, message='请填写手机号码')])
    reasion = StringField(validators=[DataRequired()])
