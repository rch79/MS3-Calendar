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


def display_main_menu():
    """
    Display main menu on screen
    """
    print("************MAIN MENU***************")
    print("* Please make your selection below *")
    print("* 1. Add a new event               *")
    print("* 2. Remove an event               *")
    print("* 3. Add a recurring event         *")
    print("* 4. Remove a recurring event      *")
    print("* 5. Add event participants        *")
    print("* 6. Remove event participants     *")
    print("* 7. Clear calendar                *")
    print("************************************\n")


def display_calendar():
    """
    Lists events in the calendar
    """
    event_count = 0
    for event in CALENDAR:
        print(event)
        event_count += 1

    if not event_count:
        print("There are no events in the calendar.")


def main():
    """
    Run main functions
    """
    display_main_menu()
    display_calendar()


print("Welcome to Kalendar")
print("A Python-based Google Calendar Interface\n")
print("Calendar URL: https://bit.ly/392Xz9R\n")
main()
