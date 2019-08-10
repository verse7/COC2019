import jwt
from flask import Blueprint, request, jsonify, session, escape, current_app
from api.model import db
from api.form import csrf
from api.model.Event import Event
from api.form.EventForm import EventForm
from api.util import form_errors, generate_api_response

bp = Blueprint('events', __name__, url_prefix='/events')

# exempt all authentication views from csrf protection because
# the csrf token will be set upon logging into the application
csrf.exempt(bp)

@bp.route('/', methods=['GET', 'POST'])
def create_event():
  if request.method == 'GET':
    events = {'events': [{'title': e.title, 'location': e.location, 
                'manpower_quota': e.manpower_quota, 'attendees': e.attendees } 
              for e in Event.query.all()]}
    
    response = generate_api_response(20, 'success', 
                ['Successfully fetched all events'], events, 200)
  else:
    form = EventForm.from_json(request.json)

    if form.validate_on_submit():
      title = form.title.data
      location = form.title.data
      manpower_quota = form.manpower_quota.data
      
      try:
        event = Event(title, location, manpower_quota)
        db.session.add(event)
        db.session.commit()
        response = generate_api_response(21, 'success', 
                    ['Successfully created event'], {}, 200)
      except:
        response = generate_api_response(41, 'error', 
                    ['A cleanup event is already created for this location'], {}, 200)
    else:
      response = generate_api_response(40, 'error', 
                form_errors(form), {}, 200)

  data, status = response
  return jsonify(data), status

