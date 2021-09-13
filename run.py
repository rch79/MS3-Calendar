import gcsa
from beautiful_date import *
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from google.oauth2.service_account import Credentials
#from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'creds.json'
CREDS = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
CALENDAR = GoogleCalendar("13mu09pc1s201mq40c0e51uics@group.calendar.google.com", credentials = CREDS)

event = Event(
    'Breakfast',
    start=(14/Sept/2021)[9:00],
    end=(14/Sept/2021)[9:45],
    event_id="12345"
    )


#CALENDAR.add_event(event)
for events in CALENDAR:
    print(events)
#print(CALENDAR)
#for event in CALENDAR:
    #print(event)
    #print(event.event_id)

#CALENDAR.delete_event(event)
#CALENDAR.clear()
for events in CALENDAR:
    print(events.id)

test = CALENDAR.get_event("m11qcka9q75aei3eimordp6mq8")
print(test)
CALENDAR.delete_event(test)
for events in CALENDAR:
    print(events.id)