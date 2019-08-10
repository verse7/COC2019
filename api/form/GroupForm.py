from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

class GroupForm(FlaskForm):
  class Meta:
    csrf = False
  name = StringField('name', validators=[InputRequired()])