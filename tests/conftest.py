import pytest
import json
from api import create_api
from api.model import db
from api.model.User import User


@pytest.fixture
def api():
  api = create_api({
    'TESTING': True,
    'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:password123@localhost/app_name_sandbox',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': 'test'
  })

  with api.app_context():
    # create a new test user if we don't have one
    if not User.query.filter_by(email='test@email.com').first():
      db.session.add(User('test@email.com', 'test'))
      db.session.commit()

  yield api


@pytest.fixture
def client(api):
  return api.test_client()


@pytest.fixture
def runner(api):
  return api.test_cli_runner()


class AuthActions(object):
  def __init__(self, client):
    self._client = client

  def login(self, email='test@email.com', password='test'):
    headers = {'Content-Type': 'application/json'}
    return self._client.post(
      '/auth/login',
      headers=headers,
      data = json.dumps({'email': email, 'password': password})
    )

  def logout(self):
    return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
  return AuthActions(client)