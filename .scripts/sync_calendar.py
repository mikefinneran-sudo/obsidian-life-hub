#!/usr/bin/env python3
"""
Sync Google Calendar events to Obsidian daily notes
Adds today's events to the daily note automatically
"""

import os
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

# For Google Calendar API
try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    import pickle
except ImportError:
    print("⚠️  Google Calendar libraries not installed yet.")
    print("Run: pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Auto-detect vault path (script is in .scripts/ folder)
SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_PATH = SCRIPT_DIR.parent
DAILY_DIR = VAULT_PATH / "Daily"
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    """Authenticate and return Google Calendar service"""
    creds = None
    token_file = VAULT_PATH / ".scripts" / "calendar_token.pickle"

    # Load existing credentials
    if token_file.exists():
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Need to create OAuth credentials first
            print("🔐 First time setup - need to authenticate with Google")
            print("\nSteps:")
            print("1. Go to: https://console.cloud.google.com/apis/credentials")
            print("2. Create OAuth 2.0 Client ID (Desktop app)")
            print("3. Download JSON and save as: ~/.config/google/credentials.json")
            print("\nThen run this script again.")
            sys.exit(1)

        # Save credentials for next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def get_todays_events(service):
    """Get today's calendar events"""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timedelta(days=1)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=today.isoformat() + 'Z',
        timeMax=tomorrow.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def add_events_to_daily_note(events, date_str=None):
    """Add calendar events to daily note"""
    if date_str is None:
        date_str = date.today().strftime('%Y-%m-%d')

    daily_note = DAILY_DIR / f"{date_str}.md"

    if not daily_note.exists():
        print(f"⚠️  Daily note for {date_str} doesn't exist yet")
        print("Run: obs-daily")
        return

    content = daily_note.read_text()

    # Build calendar section
    calendar_section = "\n## 📅 Calendar\n\n"

    if not events:
        calendar_section += "No events today\n"
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            summary = event.get('summary', 'No title')

            # Parse time
            if 'T' in start:
                time_obj = datetime.fromisoformat(start.replace('Z', '+00:00'))
                time_str = time_obj.strftime('%I:%M %p')
            else:
                time_str = 'All day'

            calendar_section += f"- **{time_str}** - {summary}\n"

    # Insert calendar section after Revenue Activities
    if "## 💰 Revenue Activities" in content:
        content = content.replace(
            "## 💰 Revenue Activities",
            f"{calendar_section}\n## 💰 Revenue Activities"
        )
    else:
        # Add before Projects section
        content = content.replace(
            "## 📊 Projects",
            f"{calendar_section}\n## 📊 Projects"
        )

    daily_note.write_text(content)
    print(f"✅ Added {len(events)} calendar events to {date_str}")

def main():
    print("📅 Google Calendar → Obsidian Sync\n")

    try:
        service = get_calendar_service()
        events = get_todays_events(service)
        add_events_to_daily_note(events)

        print(f"\n✨ Synced {len(events)} events")

        # Show events
        if events:
            print("\nToday's events:")
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(f"  • {event.get('summary', 'No title')} - {start}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you've set up Google Calendar API credentials")

if __name__ == "__main__":
    main()
