import pytest
import json
from flask import session


@pytest.mark.parametrize(('email', 'password', 'messages'), (
  ('', '', ['Error in the email field - This field is required.', 'Error in the password field - This field is required.']),
  ('a', '', ['Error in the email field - Invalid email address.', 'Error in the password field - This field is required.']),
  ('', 'b', ['Error in the email field - This field is required.']),
  ('a', 'b', ['Error in the email field - Invalid email address.']),
  ('test@email.com', '', ['Error in the password field - This field is required.']),
  ('test@email.com', 'wrongpass', ['A user already exists with these credentials']),
  ('test@email.com', 'test', ['A user already exists with these credentials'])
))
def test_register_validate_input(client, email, password, messages):
  headers = {'Content-Type': 'application/json'}
  data = json.dumps({"email": email, "password": password})
  response = client.post(
    '/auth/register',
    headers=headers,
    data=data
  )
  assert messages == json.loads(response.data)['message']


@pytest.mark.parametrize(('email', 'password', 'messages'), (
  ('', '', ['Error in the email field - This field is required.', 'Error in the password field - This field is required.']),
  ('a', '', ['Error in the email field - Invalid email address.', 'Error in the password field - This field is required.']),
  ('', 'b', ['Error in the email field - This field is required.']),
  ('a', 'b', ['Error in the email field - Invalid email address.']),
  ('test@email.com', '', ['Error in the password field - This field is required.']),
  ('test@email.com', 'wrongpass', ['Incorrect email or password']),
))
def test_login_validate_input(client, email, password, messages):
  headers = {'Content-Type': 'application/json'}
  data = json.dumps({"email": email, "password": password})
  response = client.post(
    '/auth/login',
    headers=headers,
    data=data
  )
  assert messages == json.loads(response.data)['message']


def test_login(client, auth):
  response = auth.login()
  assert response.status == '200 OK'
  with client:
    client.get('/')
    assert 'api_token' in session


def test_logout(client, auth):
  auth.login()

  with client:
    response = auth.logout()
    assert response.status == '200 OK'
    assert 'api_token' not in session