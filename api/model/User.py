from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(20), nullable=False)
  lastname = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  points = db.Column(db.Integer, nullable=False)

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = generate_password_hash(password, method='pbkdf2:sha256')
    self.points = 0
 
  def __repr__(self):
    return f"<User {self.firstname}>"