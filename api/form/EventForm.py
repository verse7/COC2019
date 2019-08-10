from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email

class EventForm(FlaskForm):
  class Meta:
    csrf = False
  title = StringField('title', validators=[InputRequired()])
  location = StringField('location', validators=[InputRequired()])
  manpower_quota = IntegerField('manpower_quota', validators=[InputRequired()])
