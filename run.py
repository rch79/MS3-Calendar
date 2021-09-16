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
    Display main menu on the screen
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
    user_selection = ""

    while user_selection not in menu_options:
        try:
            user_selection = int(input('Please type your selection (1 - 9): \n'))
            if user_selection not in menu_options:
                print("Please select a valid menu option")
        except ValueError:
            print("Invalid selection!!!!!")

    return(user_selection)


def activate_menu_option(selection):
    """
    Activate menu option based on
    user selection
    """
    if selection == 1:
        display_calendar()
    elif selection == 2:
        add_new_event()
    elif selection == 3:
        get_month_from_user()
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


def get_year_from_user():
    """
    Get year from user
    year must be equal to or higher than current year
    maximum valid year equals current year + 99 years
    """
    MIN_YEAR = D.today().year  # Min valid year is current year
    MAX_YEAR = MIN_YEAR + 99  # Max valid year is current year + 100
    year = 0

    while year not in range(MIN_YEAR, MAX_YEAR):
        try:
            year = int(input("Please enter the year of the event "
                             "in the YYYY format: \n"))
            if year not in range(MIN_YEAR, MAX_YEAR):
                print("The year must be equal to or higher than the "
                      "current year\n")
        except ValueError:
            print("You must enter a valid number in the YYYY format\n")

    print(year)
    input("Press any key to continue")
    return year


def get_month_from_user():
    """
    Get month from user
    """
    month = 0

    while month not in range (1,13):
        try:
            print("Event Month: ")
            print("1 - January")
            print("2 - February")
            print("3 - March")
            print("4 - April")
            print("5 - May")
            print("6 - June")
            print("7 - July")
            print("8 - August")
            print("9 - September")
            print("10 - October")
            print("11 - November")
            print("12 - December")
            month = int(input("\nPlease make your selection (1 - 12)\n"))

            if month not in range(1, 13):
                print("Please choose a number from 1 to 12\n")

        except ValueError:
                print("Please choose a number from 1 to 12\n")

    print(month)
    input("Press any key to continue")
    return month
            
#def test_function():
 #   event = Event(
 #   'Breakfast',
 #   start=(22/Feb/2021)[9:00],
 #   end=(12/Sept/2020)[9:45],
 #   )

 #   CALENDAR.add_event(event)

def main():
    """
    Run main functions
    """
    while True:
        display_main_menu()
        menu_option = get_user_menu_option()
        if menu_option == 9:
            print("\nThank you for using Kalendar.")
            break
        else:
            activate_menu_option(menu_option)


print("Welcome to Kalendar")
print("A Python-based Google Calendar Interface\n")
print("Calendar URL: https://bit.ly/392Xz9R\n")
main()
