from . import db
import datetime

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