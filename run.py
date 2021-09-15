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
    print("************************************")
    print("* 1. Show events in calendar       *")
    print("* 2. Add a new event               *")
    print("* 3. Remove an event               *")
    print("* 4. Add a recurring event         *")
    print("* 5. Remove a recurring event      *")
    print("* 6. Add event participants        *")
    print("* 7. Remove event participants     *")
    print("* 8. Clear calendar                *")
    print("* 9. Quit                          *")
    print("************************************\n")


def get_user_menu_option():
    """
    Get user selection of one of the main menu options
    Returns an error message if user makes an invalid selection
    """
    menu_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        try:
            user_selection = int(input('Please type your selection (1 - 9): \n'))
        except ValueError:
            print("Invalid selection!!!!!")
        else:
            if user_selection not in menu_options:
                print("Invalid selection!!!")
            else:
                return(user_selection)


def activate_menu_option(selection):
    """
    Activate menu option based on
    user selection
    """
    if selection == 1:
        display_calendar()
    else:
        pass


def display_calendar():
    """
    Lists events in the calendar
    Display message if calendar is emptyu
    """
    event_count = 0
    for event in CALENDAR:
        print(event)
        event_count += 1

    if not event_count:
        print("There are no events in the calendar.")
    
    input("\nPress any key to conrinue")


def main():
    """
    Run main functions
    """
    while True:
        display_main_menu()
        menu_option = get_user_menu_option()
        if menu_option == 9:
            print("\nThank you for using Kalendar")
            break
        else:
            activate_menu_option(menu_option)


print("Welcome to Kalendar")
print("A Python-based Google Calendar Interface\n")
print("Calendar URL: https://bit.ly/392Xz9R\n")
main()
