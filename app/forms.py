from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email






class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('Form',validators=[FileRequired(),FileAllowed(['jpg','png'])])
