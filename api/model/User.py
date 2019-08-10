import datetime
from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
  __tablename__ = "users"

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

  user_groups = db.Table('user_groups',
  db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
  db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Group(db.Model):
  __tablename__ = "groups"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  date_created = db.Column(db.Date, nullable=False, default=datetime.datetime.utcnow())
  members = db.relationship('User', secondary='user_groups', lazy=True,
    backref=db.backref('groups'))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"<Group {name}>"