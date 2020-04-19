from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField

from wtforms.validators import InputRequired



class AddPost(FlaskForm):
    title = StringField('Post Title', validators=[InputRequired()])
    body = TextAreaField('Post Body', validators=[InputRequired()])
    picture = FileField('Post Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    video = FileField('Post Video', validators=[FileAllowed(['mp4'])])

    submit = SubmitField('Save Post')


