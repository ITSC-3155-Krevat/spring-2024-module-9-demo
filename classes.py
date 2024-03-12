from typing import TypedDict

class Event(TypedDict):
  name: str

class UserEvent(TypedDict):
  name: str
  event_id: str