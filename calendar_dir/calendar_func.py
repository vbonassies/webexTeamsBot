from datetime import datetime, timedelta
import pickle
import os.path

import googleapiclient
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/calendar"]

CREDENTIALS_FILE = "credentials.json"


def get_calendar_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)
    return service


def list_calendars():
    service = get_calendar_service()
    print("Getting list of calendars")
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get("items", [])

    if not calendars:
        print("No calendar found.")
    return calendars


def list_events():
    service = get_calendar_service()
    now = datetime.today().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId="9id9jtd88ckj81tq8blkshblts@group.calendar.google.com",
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    events = events_result.get("items", [])
    if not events:
        print("No upcoming events found.")
    return events


def today_events():
    service = get_calendar_service()
    now = datetime.today().isoformat() + 'Z'
    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow = tomorrow.isoformat() + 'Z'
    events_result = service.events().list(
        calendarId="9id9jtd88ckj81tq8blkshblts@group.calendar.google.com",
        timeMin=now,
        timeMax=tomorrow,
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    events = events_result.get("items", [])
    if not events:
        print("No upcoming events found.")
    return events


def create_event(start_d, number_days, summary, description):
    service = get_calendar_service()
    start_d = datetime.strptime(start_d, "%Y-%m-%d %H:%M:%S")
    start = start_d.isoformat()
    number_days = int(number_days)
    h = 24 * number_days - 24
    end = (start_d + timedelta(hours=h)).isoformat()

    event_result = service.events().insert(calendarId="9id9jtd88ckj81tq8blkshblts@group.calendar.google.com",
                                           body={
                                               "summary": summary,
                                               "description": description,
                                               "start": {"dateTime": start, "timeZone": "Europe/Paris"},
                                               "end": {"dateTime": end, "timeZone": "Europe/Paris"}
                                           }).execute()
    return event_result


def update_event(c_id, summary, desc, s, e):
    service = get_calendar_service()

    s = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    start = s.isoformat()
    e = datetime.strptime(e, "%Y-%m-%d %H:%M:%S")
    end = e.isoformat()

    event_result = service.events().update(
        calendarId="9id9jtd88ckj81tq8blkshblts@group.calendar.google.com",
        eventId=c_id,
        body={
            "summary": summary,
            "description": desc,
            "start": {"dateTime": start, "timeZone": "Europe/Paris"},
            "end": {"dateTime": end, "timeZone": "Europe/Paris"},
        }
    ).execute()
    return event_result


def delete_event(c_id):
    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId="9id9jtd88ckj81tq8blkshblts@group.calendar.google.com",
            eventId=c_id,
        ).execute()
    except googleapiclient.errors.httpError:
        return "Failed to delete event"
    return "Event deleted"
