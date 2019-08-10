from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email

class RegistrationForm(FlaskForm):
  class Meta:
    csrf = False
  email = StringField('email', validators=[Email(), InputRequired()])
  password = StringField('password', validators=[InputRequired()])
