import os
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class CalendarHandler:
    def __init__(self):
        self.service = self.get_calendar_service()

    def get_calendar_service(self):
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            'credentials.json', scopes)
        creds = flow.run_local_server(port=0)
        service = googleapiclient.discovery.build('calendar', 'v3', credentials=creds)
        return service

    def create_event(self, summary, start_time, end_time, timezone='UTC'):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': timezone,
            },
        }

        try:
            event = self.service.events().insert(calendarId='primary', body=event).execute()
            print(f'Event created: {event.get("htmlLink")}')
        except Exception as e:
            print(f'An error occurred: {e}')