

# GCalendar-CI
[Check it out on Heroku](https://gcalendar-ci.herokuapp.com/)
[View the calendar on Google Calendar](https://bit.ly/392Xz9R)

GCalendar-CI is a Python-based command line interface program that enables the user to list, add or remove entries in a calendar. The calendar interfaces with a [public Google Calendar](https://calendar.google.com/calendar/u/0/embed?src=13mu09pc1s201mq40c0e51uics@group.calendar.google.com&ctz=Europe/Dublin).


## Features

- Add or remove events to a Google Calendar
- View events in the calendar that will happen within 10 years from the curent date
- Clear all events in the calendar happening within 10 years from the current date
- View the calendar on the Google Calendar website


  
## Target Audience

Any users who rely on Google Calendars to keep track of their appointments.


  
## User Goals
- User should be able to easily add, remove and list events in the calendar. The interface should be straightforward ans self-explanatory

## Structure
The interface was designed to be straightforwad and self-explanatory. It consists of a main menu that presents the user with five options:
#### 1. Show events in the calendar:
 - Displays events scheduled for up to 10 years from the current date. Past events will not be shown
#### 2. Add a new event:
 - Gives the user the option to add a new event, name the event, set its start and end dates and start and end times.
#### 3. Remove an event:
 - Allows users to pick and delete an event from a list showing all the events scheduled for up to 10 years from the current date
#### 4. Clear calendar
 - Allows users to clear all the events scheduled for up to 10 years from the current date (excluding past events)
#### 5. Quit
- Allows users to quit the program

## User Stories
    1. I would like to view the events that are currently in the calendar
    2. I would like to add a new event to the calendar
    3. I would like to remove an event from the calendar
    4. I would like to clear all the events from the calendar
    5. I would like to see the calendar on the Web
    6. I would like to quit the program

## Testing User Stories
1. I would like to view the events that are currently in the calendar

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| View Events in the calendar| Select option "1" on the main menu | See a list of events in the calendar from current date through the following 10 years | Works as expected |


2. I would like to add a new event to the calendar

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Add a new event|Select option "2" on the main menu|Navigate to the Add New Event menu. User will be able to add the event start and end date and time, and the event will be uploaded to the Google Calendar|Works as expected|

3. I would like to remove an event from the calendar

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Remove an event from the calendar|Select option "3" on the main menu|A list of events in the calendar will be displayed. User will type the number corresponding to the event to be deleted. The program will ask the user to confirm the selection. Event will be deleted and removed from the Google Calendar |Works as expected|

4. I would like to clear all the events from the calendar

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Clear all upcoming events from the calendar|Select option "4" on the main menu|All events ranging from current date through the following 10 years will be deleted|Works as expected|

5. I would like to see the calendar on the Web

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|See the calendar on the Web|Navigate to the [hyperlink shown at the top of the main menu on a web browser](https://bit.ly/392Xz9R)|Calendar will be displayed on the browser window |Works as expected|

6. I would like to quit the program

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Quit the program|Press "5" on the main menu|Program will shut down|Works as expected|

## Data Models

The program relies on a dictionary that is re-generated each time a change is made to the calendar. Each event is assigned an integer as a key. Each key is paired with a unique event id that is automatically generated everyt time a new event is created. The program will iterate through the events that are currently in the calendar (starting from the current date/ time onwards through the following 10 years) and make the key assignments at each iteration, staring with number "1" for the event that is closest to the current date. This key / pair arrangengement works well for task such as "Remove an event", in which a list of events is presented to the user in chronological order. The user in this case will simply input the integer associated with the event, and the integer happens to be the event key.

Since the dictionary is accessed and modified by more than one menu option, I decided to make it a global variable.


## Validation
### PEP8 Validation
No issues were found with the code using the [PEP8 Online Check Tool](http://pep8online.com/):
<img src="https://github.com/rch79/MS3-Calendar/blob/main/assets/images/pep8_validation_screengrab.PNG"></img>

## Technologies Used

### Programming Language:
 - Python 3
### Applications and Platforms
 - [Git](https://git-scm.com/) - CLI-based version control software available on Gitpod
 - [GitHub](https://github.com/) - Project repository
 - [Gitpod](https://www.gitpod.io/) - A Container-based development platform on which some of the coding was written
 - [Sublime Text](https://www.sublimetext.com/) - Some of the code was written on Sublime text - especially when additional screen real estate was needed. TThe following plugins were used in conjunction with Sublime Text:
   - [Anaconda](http://damnwidget.github.io/anaconda/) - A Python IDE for Sublime text - useful for showing documentation, highlighting PEP8 violations, code autocompletion etc
   - [SublimeREPL](https://github.com/wuub/SublimeREPL) - For interpreting Python code within an editor tab
 - [GitHub Desktop](https://desktop.github.com/) - For uploading code changes to the project GitHub repository when coding was done on Sublime text
 - [Heroku](https://www.heroku.com/) - A cloud application platform used for deployment of the program
 - [Readme.So](https://readme.so/) - A web-based editor for easy README file creation
 - [bitly](https://bitly.com/) - Used to shorten the Google Calendar URL

 ### Python Libraries:
 - [datetime](https://docs.python.org/3/library/datetime.html) - For manipulation of date and time objects
 - [pytz](https://pypi.org/project/pytz/) - For performing timezone calculations
 - [dateutil](https://dateutil.readthedocs.io/en/stable/index.html) - An extension to the datetime module. Useful for performing timeshift operation on datetime objects (add 10 years to a date, for instance)
 ### Third-party Libraries:
 - [Google Calendar Simple API (gcsa)](https://google-calendar-simple-api.readthedocs.io/en/latest/) - A simplified adaptation of the official Google Calendar API
 - [google.oauth2.service_account.Credentials](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) - Enables the interaction between the program and Google services (such as Google Calendar)


## Deployment
The program was deployed on [Heroku]((https://www.heroku.com/)), using the following steps:
- Create an account on Heroku
- On the user account page, click on "new", and "Create new app"
- On the "Settings" tab, navigate to "Config Vars":
  - Click on "Reveal Config Vars"
  - On the key field type CREDS. On the Value field copy and paste the entire contents of your credential.json file
  - Click on "Add"
- Still on the settings tab, navigate to Buildpacks:
  - Click on "Add buildpack"
  - Select Python
  - Save changes
  - Repeat the process above to add node.js
  - Make sure Python is displayed above node.js. If that is not the case rearrange the order by clicking ad dragging the buildpacks
- Deploy tab:
  - Deploy method: GitHub
  - Click on "Connect to GitHub"
  - Select the repository for the program       being deployed
  - Click on "connect"
  - Select one of the following options:
    - Automatic deploy: Heroku will rebuild the app every time a change is pushed to the GitHub repository
    - Manual deploy: Heroku will only rebuild the app when the user chooses to do so.
- Required Python dependencies were added to the "requirements.txt" file using the "pip freeze > requirements.txt" CLI command on Gitpod. This file is used by Heroku to install the dependencies used in the program

## Acknowledgements
- Code Insitute staff and program materials - always very helpful
- A huge thank you to my mentor Spence Barriball
 