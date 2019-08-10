from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired
from .JSONField import JSONField

class EventForm(FlaskForm):
  class Meta:
    csrf = False
  image = FileField('photo', validators=[FileAllowed(['jpg','jpeg', 'Only jpeg images are accepted!'])])
  details = JSONField('details', validators=[InputRequired()])
