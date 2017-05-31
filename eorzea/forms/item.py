from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from wtforms.fields import StringField
from wtforms.fields import TextAreaField
from wtforms.fields import SubmitField
from wtforms.fields import FieldList
from wtforms.validators import DataRequired
from wtforms.validators import Length


class ItemForm(Form):
    title = StringField(validators=[DataRequired(), Length(max=20)])
    description = TextAreaField(validators=[DataRequired(), Length(max=512)])
    images = FieldList(
        FileField('image', validators=[FileRequired(),
                                       FileAllowed(['jpg', 'png'], 'Image only!')]),
        validators=[DataRequired()],
        min_entries=1, max_entries=3)
    location = StringField(validators=[DataRequired(), Length(max=128)])
    add_image = SubmitField()


class ItemCommentForm(Form):
    content = TextAreaField(validators=[DataRequired(), Length(max=512)])
