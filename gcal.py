from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load the credentials
credentials = service_account.Credentials.from_service_account_file('credentials.json')

# Build the service
service = build('calendar', 'v3', credentials=credentials)

# Specify the ID of the calendar
calendar_id = '76a6c8f8e4005dbb88dcb2f4b10ab20916f1777664bfdc27349bf902f04e0b53@group.calendar.google.com'

# Get the events from the calendar
events_result = service.events().list(calendarId=calendar_id, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

for event in events:
    print(event)
    input()
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
