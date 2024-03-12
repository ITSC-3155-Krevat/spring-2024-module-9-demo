from uuid import uuid4
from flask import Flask, render_template, request, redirect, abort
from classes import UserEvent, Event
from utils import find_users_for_event, is_user_registered_for_event
# from utils import calculate_mean


app = Flask(__name__)

events: dict[str, Event] = {
  'e95e4f66-bed3-4d2d-a2e7-16a3247f45c0': {
    'name': 'Pack Halton'
  },
  'e942a41f-b5c1-49ed-a5fb-11d83fbb9f4f': {
    'name': 'DBD Tourney'
  },
  'a5905b69-c0b4-489b-b569-4d771486116a': {
    'name': 'SWE Brainstorming'
  },
  '924259ba-b2e6-4337-9c8f-2bdcbdd251f2': {
    'name': 'Cook Out Hangout'
  },
  '4c89d3b5-0ca4-4cae-95ae-02ac66b0a332': {
    'name': 'Board Games @ Woodward'
  },
}

user_events: dict[str, UserEvent] = {
}

@app.get('/')
def index():
  return render_template('index.html')

@app.get('/events')
def view_events():
  return render_template('events.html', events=events, user_events=user_events)

@app.get('/events/new')
def new_event():
  return render_template('new_event.html', events=events)

@app.post('/events/new')
def create_event():
  name = request.form.get('name', type=str)
  event_id = request.form.get('event_id', type=str)

  if not event_id or not name:
    abort(400)

  if event_id not in events.keys():
    abort(400)

  if is_user_registered_for_event(user_events, name, event_id):
    abort(400)

  user_events[str(uuid4())] = {
    'name': name,
    'event_id': event_id
  }

  return redirect('/events')

@app.get('/events/<user_event_id>')
def view_event(user_event_id: str):
  if user_event_id not in user_events.keys():
    abort(404)
  user_event = user_events[user_event_id]
  registered_users = find_users_for_event(user_events, user_event['event_id'])
  del registered_users[user_event_id]
  return render_template('event.html', user_event_id=user_event_id, user_event=user_event, event=events[user_event['event_id']], registered_users=registered_users)

@app.post('/events/<user_event_id>/delete')
def delete_event(user_event_id: str):
  if user_event_id not in user_events.keys():
    abort(404)
  del user_events[user_event_id]
  return redirect('/events')