from flask_wtf.csrf import generate_csrf

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


def generate_api_response(code, status, msg, data, http_status):
  # always generate a new csrf token on each response for xss protection
  data['csrf_token'] = generate_csrf()
  return {'code': code,'status': status, 'message': msg, 'data': data,}, http_status