
# GCalendar

GCalendar is a Python-based command line interface program that enables the user to list, add or remove entries in a calendar. The calendar interfaces with a [public Google Calendar](https://calendar.google.com/calendar/u/0/embed?src=13mu09pc1s201mq40c0e51uics@group.calendar.google.com&ctz=Europe/Dublin).


## Features

- Add or remove events to a Google Calendar
- View events in the calendar that will happen within a year from the curent date
- Clear all events in the calendar happening within a year from the current date


  
## Target Audience

Any users who rely on Google Calendars to keep track of their appointments.


  
## User Goals
- User should be able to easily add, remove and list events in the calendar. The interface should be straightforward ans self-explanatory

## Structure
The interface was designed to be straightforwad and self-explanatory. It consists of a main menu that presents the user with five options:
#### 1. Show events in the calendar:
 - Displays events scheduled for up to a year from the current date
#### 2. Add a new event:
 - Gives the user the option to add a new event, name the event, set its start and end dates and start and end times.
#### 3. Remove an event:
 - Allows users to pick and delete an event from a list showing all the events scheduled for up to a year from the current date
#### 4. Clear calendar
 - Allows users to clear all the events scheduled for up to a year from the current date
#### 5. Quit
- Allows users to quit the program

## User Stories
    1. I would like to view the events that are currently in the calendar
    2. I would like to add a new event to the calendar
    3. I would like to remove an event from the calendar
    4. I would like to clear all the events from the calendar
    5. I would like to quit the program

## Data Models

The program relies on a dictionary that is re-generated each time a change is made to the calendar. Each event is assigned an integer as a key. Each key is paired with a unique event id that is automatically generated everyt time a new event is created. Prior to being added to the dictionary, the list of events is added to a list that is sorted in chronological order. The program will then iterate through the list and make the key assignments at each iteration, staring with number "1" for the event that is closest to the current date. This key / pair arrangengement works well for task such as "Remove an event", in which a list of events is presented to the user in chronological order. The user in this case will simply input the integer associated with the event, and the integer happens to be the event key.

Since the dictionary is accessed and modified by more than one menu option, I decided to make it a global variable.

## Technologies Used

### Programming Language:
 - Python 3
### Applications and Platforms
 - Git - CLI-based version control software available on Gitpod
 - GitHub - Project repository
 - Gitpod - A Container-based development platform on which some of the coding was written
 - Sublime Text - Some of the code was written on Sublime text - especially when additional screen real estate was needed. TThe following plugins were used in conjunction with Sublime Text:
   - Anaconda - A Python IDE for Sublime text - useful for showing documentation, highlighting PEP8 violations, code autocompletion etc
   - SublimeREPL - For interpreting Python code within an editor tab
 - GitHub for Windows - For uploading code changes to the project GitHub repository when coding was done on Sublime text
 - Heroku - Used for deployment of the program
 - Readme.So - A web-based editor for easy README file creation

 ### Python Libraries:
 - datetime - For manipulation of date and time objects

 ### Third-party Libraries:
 - Google Calendar Simple API (gcsa) - A simplified adaptation of the official Google Calendar API
 - google.oauth2.service_account.Credentials - holds OAuth 2.0 credentials that authorize access to Google services (such as Google Calendar)


## Deployment
The program was deployed on Heroku, using the following steps:
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
  - Select the repository for the program being deployed
  - Click on "connect"
  - Select one of the following options:
    - Automatic deploy: Heroku will rebuild the app every time a change is pushed to the GitHub repository
    - Manual deploy: Heroku will only rebuild the app when the user chooses to do so.
- Required Python dependencies were added to the "requirements.txt" file using the "pip freeze > requirements.txt" CLI command on Gitpod. This file is used by Heroku to install the dependencies used in the program

## Acknowledgements
- Code Insitute staff and program materials - always very helpful
- A huge thank you to my mentor Spence Barriball
 