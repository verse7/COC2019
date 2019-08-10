import jwt
from flask import Blueprint, request, jsonify, session, escape, current_app
from api.model import db
from api.form import csrf
from api.model.Group import Group
from api.model.User import User 
from api.form.GroupForm import *
from api.util import form_errors, generate_api_response, gives_user

bp = Blueprint('user', __name__, url_prefix='/user')
csrf.exempt(bp)

@bp.route('/points', methods=['GET'])
def points():
    try:
        #get event_id and user_id parameters
        user_id = request.args.get('user')
        
        #find user with matching id
        user = User.query.filter_by(id=user_id).first()

        points = {"points": user.points}
        response = generate_api_response(20, 'success', 
                    ['Successfully fetched user points'], points, 200)
    except:
        response = generate_api_response(41, 'error', 
                    ['An error has occurred'], {}, 200)

    data, status = response
    return jsonify(data), status
