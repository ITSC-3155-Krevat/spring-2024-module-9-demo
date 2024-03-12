from classes import UserEvent

def find_users_for_event(user_events: dict[str, UserEvent], event_id: str) -> dict[str, UserEvent]:
  """
  Finds all users registered for a given event.

  Args:
    user_events (dict[str, UserEvent]): A dictionary of user events.
    event_id (str): The ID of the event to search for.

  Returns:
    dict[str, UserEvent]: A dictionary of user events for the given event.
  """
  users = {}
  for user_event_id, user_event in user_events.items():
    if user_event['event_id'] == event_id:
      users[user_event_id] = user_event
  return users

def is_user_registered_for_event(user_events: dict[str, UserEvent], user_name: str, event_id: str) -> bool:
  """
  Checks if a user, specificallt their name, is registered for a given event.

  Args:
    user_events (dict[str, UserEvent]): A dictionary of user events.
    user_name (str): The name of the user to search for.
    event_id (str): The ID of the event to search for.

  Returns:
    bool: True if the user is registered for the event, False otherwise.
  """
  for user_event in user_events.values():
    if user_event['name'] == user_name and user_event['event_id'] == event_id:
      return True
  return False