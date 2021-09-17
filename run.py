import gcsa
from beautiful_date import *
import datetime
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from google.oauth2.service_account import Credentials
#from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'creds.json'
CREDS = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,
                                              scopes=SCOPES)
CALENDAR = GoogleCalendar("13mu09pc1s201mq40c0e51uics@group.calendar.google.com", credentials=CREDS)

month_dictionary = {1: "January", 2: "February", 3: "March", 4: "April",
                    5: "May", 6: "June", 7: "July", 8: "August",
                    9: "September", 10: "October", 11: "November",
                    12: "December"}


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
    print("* 84. Test get_date function       *")
    print("* 85. Test get_time function       *")
    print("* 86. Add test event               *")
    print("* 9. Quit                          *")
    print("************************************\n")


def get_user_menu_option():
    """
    Get user selection of one of the main menu options
    Returns an error message if user makes an invalid selection
    """
    menu_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 84, 85, 86]
    user_selection = ""

    while user_selection not in menu_options:
        try:
            user_selection = int(input(
                                        "Please type your "
                                        "selection (1 - 9): \n"
                                        ))
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
    elif selection == 84:
        get_date_from_user("start")
    elif selection == 85:
        get_time_from_user("start")
    elif selection == 86:
        pass
    else:
        pass


def display_calendar():
    """
    Lists upcoming events in the calendar
    Display message if calendar is empty
    Past events will not be shown
    """
    event_count = 0
    for event in CALENDAR:
        print(event)
        event_count += 1

    if not event_count:
        print("There are no events in the calendar.")

    input("\nPress any key to conrinue")


def get_date_from_user(start_or_end):
    """
    Get event date from user
    Displays error message if date is invalid
    Takes a string as a parameter to display correct message
    """
    is_date_valid = False
    yes_or_no = ""

    while not is_date_valid:
        yes_or_no = ""  # resets yes_or_no variable

        try:
            date_str = input(
                             f"Please enter the {start_or_end} date "
                             "in MM-DD-YYYY format: \n"
                             )
            date_list = date_str.split("-")
            date_list = [int(string) for string in date_list]
            chosen_date = datetime.date(date_list[2],
                                        date_list[1],
                                        date_list[0])
        except ValueError:
            print("Invalid date")
        else:
            print(
                  f"\nThe date you selected is {date_list[0]} "
                  f"{month_dictionary[date_list[1]]}, {date_list[2]}"
                  )

            while yes_or_no not in ["Y", "y", "n", "N"]:
                yes_or_no = input("\nIs that correct (Y/N)? \n")

            if yes_or_no in ["Y", "y"]:
                is_date_valid = True

    return chosen_date


def get_time_from_user(start_or_end):
    """
    Get time from user in HH:MM 24h format
    """
    is_valid_time = False

    while not is_valid_time:
        try:
            time_str = input(f"Please enter the event {start_or_end} time in HH:MM 24h format:\n")
            time_list = time_str.split(":")
            time_list = [int(num) for num in time_list]
            chosen_time = datetime.time(time_list[0], time_list[1])
        except ValueError:
            print("Please enter a valid time in the HH:MM format")
        else:
            is_valid_time = True

    return chosen_time


def add_new_event():
    event_name = input("Please eneter the name of the event: \n")
    event_start_date = get_date_from_user("start")
    event_end_date = get_date_from_user("end")
    event_start_time = get_time_from_user("start")
    event_end_time = get_time_from_user("end")

    event_start_datetime = datetime.datetime.combine(event_start_date, event_start_time)
    event_end_datetime = datetime.datetime.combine(event_end_date, event_end_time)

    new_event = Event(
                    event_name,
                    start=event_start_datetime,
                    end=event_end_datetime
                     )

    print("\nAdding event")
    CALENDAR.add_event(new_event)
    input("\nEvent added succesfully. Press any key to continue")

""" def add_test_event():
    event = Event(
        'Breakfast',
        start=(1 / Jan / 2019)[9:00],
        recurrence=[
            Recurrence.rule(freq=DAILY),
            Recurrence.exclude_rule(by_week_day=[SU, SA]),
            Recurrence.exclude_times([
                (19 / Apr / 2019)[9:00],
                (22 / Apr / 2019)[9:00]
            ])
        ],
        minutes_before_email_reminder=50
) """



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

""" print("start print")
for events in CALENDAR:
    print(events)
print("end print") """
""" event = Event(
    'Breakfast',
    start=(18/Sept/2021)[9:00],
    end=(18/Sept/2021)[9:45],
    event_id="12345"
    )

CALENDAR.add_event(event) """
