from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def __init__(self, email, password):
    self.email = email
    self.password = generate_password_hash(password, method='pbkdf2:sha256')