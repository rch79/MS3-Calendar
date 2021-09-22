import datetime  # for manipulating date and time objects
import pytz  # for adding timezone data to datetime objects
from dateutil.relativedelta import relativedelta  # datetime extension
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from google.oauth2.service_account import Credentials


SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'creds.json'
CREDS = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
CALENDAR = GoogleCalendar(
    "13mu09pc1s201mq40c0e51uics@group.calendar.google.com", credentials=CREDS)

TIMEZONE = pytz.timezone("Europe/Dublin")
NOW = datetime.datetime.now(TIMEZONE)  # current time
TODAY = datetime.datetime.combine(NOW, datetime.time.min)
FUTURE = TODAY + relativedelta(years=+10)  # equals today's date plus 10 years


def build_event_id_dictionary():
    """
    Build a dictionary of unique event ids used to manipulate
    the calendar
    """
    event_id_dictionary = {}
    idx = 1

    # Adds events to dictionary in chronological order
    # from range TODAY to FUTURE, using the option startTime
    for event in CALENDAR[NOW:FUTURE:'startTime']:
        event_id_dictionary[idx] = event.id
        idx += 1

    return event_id_dictionary


def display_main_menu():
    """
    Display main menu on the screen
    """
    print("Calendar URL: https://bit.ly/392Xz9R\n")
    print("************MAIN MENU***************")
    print("* Please make your selection below *")
    print("************************************")
    print("* 1. Show events in calendar       *")
    print("* 2. Add a new event               *")
    print("* 3. Remove an event               *")
    print("* 4. Clear calendar                *")
    print("* 5. Quit                          *")
    print("************************************\n")


def get_user_menu_option():
    """
    Get user selection of one of the main menu options
    Returns an error message if user makes an invalid selection
    """
    menu_options = [1, 2, 3, 4, 5]
    user_selection = ""

    while user_selection not in menu_options:
        try:
            user_selection = int(input("Please type your selection "
                                       f"(1 - {len(menu_options)}): \n"))
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
        remove_event()
    elif selection == 4:
        clear_calendar()
    else:
        pass


def print_event_details(type, index, id):
    """
    Formats and prints the details of an event
    in the calendar.
    """
    event_id = id
    idx = index
    event = CALENDAR.get_event(event_id)

    if type == "full_detail":
        event_start_str = event.start.strftime("%a, %b %d %Y at %H:%M")
        event_end_str = event.end.strftime("%a, %b %d %Y at %H:%M")

        print("********************************"
              "**********************************")
        print(f"{idx} - {event.summary}")
        print(f"Start: {event_start_str}")
        print(f"End:   {event_end_str}")
        print("********************************"
              "**********************************\n\n")

    if type == "low_detail":
        event_start_str = event.start.strftime("%d %b %y at %H:%M")
        event_end_str = event.end.strftime("%d %b %y at %H:%M")

        print(f"{idx}: {event.summary}, "
              f"from {event_start_str} to {event_end_str}")


def display_calendar():
    """
    List events in the calendar from start of
    current day to 10 years from current date
    Past events will not be shown
    """
    number_of_events = len(event_id_dict)

    # Customizes message according to number of events in the calendar
    if number_of_events == 0:
        print("\nThere are no upcoming events in the calendar\n")
    else:
        if number_of_events == 1:
            print("\nThere is 1 upcoming event in your calendar: \n\n")
        else:
            print(f"There are {number_of_events} events in your calendar\n\n")

        print("Showing events for up to 10 years from the current date\n")
        print("Past events will not be shown\n")

        for idx, event in enumerate(event_id_dict, start=1):
            print_event_details("full_detail", idx, event_id_dict[idx])

            # Requires user input after two events are displayed to
            # show additional events, unless last event is being shown
            if idx % 2 == 0 and idx != number_of_events:
                input("Press any key to show additional events")

    input("\nPress any key to go back to the main menu\n")


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
            date_str = input(f"Please enter the {start_or_end} date "
                             "in DD-MM-YYYY format: \n")
            date_list = date_str.split("-")
            date_list = [int(string) for string in date_list]
            chosen_date = datetime.date(date_list[2],
                                        date_list[1],
                                        date_list[0])
        except ValueError:
            print("Invalid date")
        else:
            print(f"\nThe date you selected is "
                  f"{chosen_date.strftime('%A, %B %d %Y')}")

            while yes_or_no not in ["Y", "y", "n", "N"]:
                yes_or_no = input("\nIs that correct (Y/N)? \n")

            if yes_or_no in ["Y", "y"]:
                is_date_valid = True

    return chosen_date


def get_time_from_user(start_or_end):
    """
    Get time from user in HH:MM 24h format
    """

    while True:
        try:
            time_str = input(f"Please enter the event {start_or_end} "
                             "time in HH:MM 24h format:\n")
            time_list = time_str.split(":")
            time_list = [int(num) for num in time_list]
            chosen_time = datetime.time(time_list[0], time_list[1])
        except ValueError:
            print("Please enter a valid time in the HH:MM format")
        except IndexError:
            print("Please enter a valid time in the HH:MM format")
        else:
            break

    return chosen_time


def add_new_event():
    """
    Create a new event based on start and end date and time
    provided by user and add it to the Google calendar, and
    updates the event id dictionary to include the new event
    """
    global event_id_dict
    date_str_format = "%a, %b %d %Y at %H:%M"

    event_name = input("Please enter the name of the event: \n")

    # get event start date and time from user
    while True:
        event_start_date = get_date_from_user("start")
        event_start_time = get_time_from_user("start")
        event_start_datetime = datetime.datetime.combine(
            event_start_date, event_start_time)
        event_start_datetime = TIMEZONE.localize(event_start_datetime)

        # check if event is starting now or in the future
        if event_start_datetime <= NOW:
            print("\nEvent must start after "
                  f"{NOW.strftime(date_str_format)}\n")
        else:
            break

    # get event end date and time from user
    while True:
        event_end_date = get_date_from_user("end")
        event_end_time = get_time_from_user("end")
        event_end_datetime = datetime.datetime.combine(
            event_end_date, event_end_time)
        event_end_datetime = TIMEZONE.localize(event_end_datetime)

        # Check if event ends after event start
        if event_end_datetime <= event_start_datetime:
            print("\nEvent must end after "
                  f"{event_start_datetime.strftime(date_str_format)}\n")
        else:
            break

    # add new event to the calendar
    new_event = Event(
        event_name, start=event_start_datetime,
        end=event_end_datetime, timezone="Europe/Dublin")

    print("\nAdding event")
    CALENDAR.add_event(new_event)
    input("\nEvent added succesfully. Press any key to "
          "go back to the main menu\n")
    event_id_dict = build_event_id_dictionary()


def remove_event():
    global event_id_dict
    number_of_events = len(event_id_dict)
    user_input = ""
    yes_or_no = ""

    while True:
        print(f"There are {number_of_events} events in the calendar: \n")

        # Lists events in low detail
        for idx, event in enumerate(event_id_dict, start=1):
            print_event_details("low_detail", idx, event_id_dict[idx])

        try:
            while user_input not in range(0, number_of_events + 1):
                user_input = int(
                    input("\nPlease select the event to "
                          f"be deleted (1 - {number_of_events}) "
                          "or press 0 to go back to the main menu\n"))
                if user_input not in range(0, number_of_events + 1):
                    print("\nInvalid selection\n")
        except ValueError:
            print("Invalid selection!")
        else:
            if user_input == 0:
                break
            else:
                while yes_or_no not in ["Y", "y", "N", "n"]:
                    print("\nThe following event will be deleted: ")
                    print_event_details(
                        "full_detail", user_input, event_id_dict[user_input])
                    yes_or_no = input("\nPlease confirm your "
                                      "selection (Y/N)\n")

                if yes_or_no in ["Y", "y"]:
                    print("Deleting event")
                    event = CALENDAR.get_event(event_id_dict[user_input])
                    CALENDAR.delete_event(event)
                    event_id_dict = build_event_id_dictionary()
                    print("Event successfully deleted\n")
                    input("Press any key to go back to the main menu")
                    break
                else:
                    break


def clear_calendar():
    '''
    Clear all events in the calendar from current date through
    10 years from current date
    '''
    global event_id_dict
    response = ""
    valid_responses = ["Y", "N"]

    if len(event_id_dict) == 0:
        print("\nThere are no events in the calendar\n")
        input("Press any key to return to the main menu\n")
    else:
        while True:
            try:
                while response not in valid_responses:
                    print("\nAll upcoming events in the next 10 "
                          "years will be deleted")
                    response = input("Would you like "
                                     "to proceed? (Y/N)").upper()
                    if response not in valid_responses:
                        print("Please type Y or N")
            except ValueError:
                print("\nPlease type Y or N")
            else:
                if response == "N":
                    input("\nPress any key to return to the main menu")
                    break
                elif response == "Y":
                    print("\nClearing calendar")

                    for idx, event in enumerate(event_id_dict, start=1):
                        event = CALENDAR.get_event(event_id_dict[idx])
                        CALENDAR.delete_event(event)

                    event_id_dict = build_event_id_dictionary()
                    input("\nDone. Press any key to go back "
                          "to the main menu\n")
                    break
                else:
                    continue


def main():
    """
    Run main functions
    """
    while True:
        display_main_menu()
        menu_option = get_user_menu_option()
        if menu_option == 5:
            print("\nThank you for using GCalendar-CI.")
            break
        else:
            activate_menu_option(menu_option)


print("Welcome to GCalendar-CI")
print("A Python-based Google Calendar Interface\n")
event_id_dict = build_event_id_dictionary()
main()
