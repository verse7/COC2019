import os
from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room

def create_api(test_config=None):
  api = Flask(__name__)

  if test_config is None:
    api.config.from_pyfile('config.py', silent=True)
  else:
    api.config.from_mapping(test_config)

  from flask_cors import CORS
  CORS(api, resources={r'*': {'origins': '*'}})

  from api.model import db
  db.init_app(api)

  from api.form import csrf
  csrf.init_app(api)

  from api.ws import socketio
  socketio.init_app(api, cors_allowed_origins='*')

  @socketio.on('join')
  def on_join(data):
    join_room(data)

  @socketio.on('leave')
  def on_leave(data):
    leave_room(data)

  from api.view import auth
  from api.view import event
  from api.view import group
  from api.view import user
  api.register_blueprint(auth.bp)
  api.register_blueprint(event.bp)
  api.register_blueprint(group.bp)
  api.register_blueprint(user.bp)

  return api
