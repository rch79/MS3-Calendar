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
CALENDAR = GoogleCalendar("13mu09pc1s201mq40c0e51uics@group.calendar.google.com", credentials=CREDS)


def main():
    """
    Runs main functions
    """
    for event in CALENDAR:
        print(event)


print("Welcome to Kalendar")
print("A Python-based Google Calendar Interface")
print("Calendar URL: https://bit.ly/392Xz9R")
main()
