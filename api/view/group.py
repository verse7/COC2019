import jwt
from flask import Blueprint, request, jsonify, session, escape, current_app
from api.model import db
from api.form import csrf
from api.model.Group import *
from api.model.User import * 
from api.form.GroupForm import *
from api.util import form_errors, generate_api_response, gives_user

bp = Blueprint('groups', __name__, url_prefix='/groups')
csrf.exempt(bp)

@bp.route('/', methods=["POST"]) 
@gives_user
def create_group(user):
  form = GroupForm.from_json(request.json)

  if form.validate_on_submit():
    name = form.name.data

    # try:
    group = Group(name)
    print(user)
    group.members.append(user)
    db.session.add(group)
    db.session.commit()

    data = {}
    data['id'] = group.id
    data['name'] = group.name

    response = generate_api_response(21, 'success',
                ['Successfully created group'], data, 200)

  else:
    response = generate_api_response(40, 'error', 
                form_errors(form), {}, 200)

  data, status = response
  return jsonify(data), status
    
