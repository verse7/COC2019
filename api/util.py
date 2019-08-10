from flask_wtf.csrf import generate_csrf
from functools import wraps
from flask import request
from .model.User import User

def form_errors(form):
  error_messages = []
  for field, errors in form.errors.items():
    for error in errors:
      message = u"Error in the %s field - %s" % (
              getattr(form, field).label.text,
              error
          )
      error_messages.append(message)

  return error_messages

def gives_user(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    email = request.headers.get('email')
    if not email:
      return generate_api_response(40, "error", ['Email header not present'], {}, 200)

    user = User.query.filter_by(email=request.headers.get('email')).first()
    return f(user, *args, **kwargs)
  return decorated



def generate_api_response(code, status, msg, data, http_status):
  # always generate a new csrf token on each response for xss protection
  data['csrf_token'] = generate_csrf()
  return {'code': code,'status': status, 'message': msg, 'data': data,}, http_status