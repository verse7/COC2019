import jwt
from flask import Blueprint, request, jsonify, session, escape, current_app
from werkzeug.security import check_password_hash
from api.model import db
from api.form import csrf
from api.model.User import User
from api.form.RegistrationForm import RegistrationForm
from api.util import form_errors, generate_api_response

bp = Blueprint('auth', __name__, url_prefix='/auth')

# exempt all authentication views from csrf protection because
# the csrf token will be set upon logging into the application
csrf.exempt(bp)

@bp.route('/register', methods=['POST'])
def register():
  form = RegistrationForm.from_json(request.json)

  if form.validate_on_submit():
    firstname = escape(form.firstname.data)
    lastname = escape(form.lastname.data)
    email = escape(form.email.data)
    password = escape(form.password.data)
    
    # try:
    user = User(firstname, lastname, email, password)
    db.session.add(user)
    db.session.commit()

    data = {}
    data['id'] = user.id
    data['firstname'] = user.firstname
    data['lastname'] = user.lastname
    data['email'] = user.email

    response = generate_api_response(21, 'success', 
                ['Successfully registered user'], data, 200)
    # except:
    #   response = generate_api_response(41, 'error', 
    #               ['A user already exists with these credentials'], {}, 200)

  else:
    response = generate_api_response(40, 'error', 
                form_errors(form), {}, 200)

  data, status = response
  return jsonify(data), status


@bp.route('/login', methods=['POST'])
def login():
  form = RegistrationForm.from_json(request.json)

  if form.validate_on_submit():
    email = escape(form.email.data)
    password = escape(form.password.data)
    
    # try to find a user with a matching email address
    user = User.query.filter_by(email=email).first()

    if user:
      if check_password_hash(user.password, password):
        token = jwt.encode({'id': user.id}, 
                          current_app.config['SECRET_KEY'], 
                          algorithm='HS256').decode('utf-8')
        # set the token on the response cookie with http only
        # and add the csrf token for subsequent responses
        session.clear()
        session['api_token'] = token
        response = generate_api_response(20, 'success', 
                  ['Login Successful'], {}, 200)
      else:
        response = generate_api_response(43, 'error', 
                  ['Incorrect email or password'], {}, 200)
    else:
      response = generate_api_response(43, 'error', 
                ['Incorrect email or password'], {}, 200)
  else:
    response = generate_api_response(40, 'error', 
                form_errors(form), {}, 200)

  data, status = response
  return jsonify(data), status


@bp.route('/logout')
def logout():
  session.clear()

  data, status = generate_api_response(20, 'success', 
                ['Successfully logged out'], {}, 200)
  return jsonify(data), status

