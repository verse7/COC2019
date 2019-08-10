from api import create_api

def test_config():
  assert not create_api().testing
  assert create_api({
    'TESTING': True,
    # added below to silence a warning
    'SQLALCHEMY_DATABASE_URI': ''
  }).testing

  