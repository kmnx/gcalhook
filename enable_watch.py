from googleapiclient.discovery import build
from google.oauth2 import service_account

# Load the credentials
credentials = service_account.Credentials.from_service_account_file('credentials.json')

# Build the service
service = build('calendar', 'v3', credentials=credentials)

# Specify the ID of the calendar to watch
calendar_id = '76a6c8f8e4005dbb88dcb2f4b10ab20916f1777664bfdc27349bf902f04e0b53@group.calendar.google.com'

# Create a unique ID for your channel
channel_id = '777376a6c8f8e4005dbb88dcb2f4b10ab20916f1777664bf3'

# Specify the URL of your notification endpoint
webhook_url = 'https://test.chunt.org:8000/notifications'

# Create a new channel
channel = service.events().watch(
    calendarId=calendar_id,
    body={
        'id': channel_id,
        'type': 'web_hook',
        'address': webhook_url
    }
).execute()

resource_id = channel['resourceId']
print('Resource ID:', resource_id)
