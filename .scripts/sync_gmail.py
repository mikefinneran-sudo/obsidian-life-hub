#!/usr/bin/env python3
"""
Sync important Gmail messages to Obsidian inbox
Creates notes for important emails to process later
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import re

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    import pickle
    import base64
except ImportError:
    print("⚠️  Gmail libraries not installed yet.")
    print("Run: pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Auto-detect vault path (script is in .scripts/ folder)
SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_PATH = SCRIPT_DIR.parent
INBOX_DIR = VAULT_PATH / "Inbox"
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Create inbox directory
INBOX_DIR.mkdir(exist_ok=True)

def get_gmail_service():
    """Authenticate and return Gmail service"""
    creds = None
    token_file = VAULT_PATH / ".scripts" / "gmail_token.pickle"

    if token_file.exists():
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("🔐 First time setup - need to authenticate with Gmail")
            print("\nSteps:")
            print("1. Go to: https://console.cloud.google.com/apis/credentials")
            print("2. Enable Gmail API")
            print("3. Create OAuth 2.0 Client ID (Desktop app)")
            print("4. Download JSON and save as: ~/.config/google/credentials.json")
            print("\nThen run this script again.")
            sys.exit(1)

        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def get_important_emails(service, max_results=10):
    """Get unread emails from important senders or with specific labels"""

    # Query for important emails
    query = 'is:unread (is:important OR label:action-needed OR from:customer)'

    results = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=max_results
    ).execute()

    messages = results.get('messages', [])

    email_data = []
    for msg in messages:
        message = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='full'
        ).execute()

        # Extract headers
        headers = message['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        from_addr = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), '')

        # Extract body
        if 'parts' in message['payload']:
            parts = message['payload']['parts']
            body = parts[0]['body'].get('data', '')
        else:
            body = message['payload']['body'].get('data', '')

        if body:
            body = base64.urlsafe_b64decode(body).decode('utf-8', errors='ignore')

        email_data.append({
            'id': msg['id'],
            'subject': subject,
            'from': from_addr,
            'date': date,
            'body': body[:1000]  # First 1000 chars
        })

    return email_data

def create_inbox_note(email):
    """Create Obsidian note for email"""

    # Clean subject for filename
    safe_subject = re.sub(r'[^a-zA-Z0-9\s-]', '', email['subject'])
    safe_subject = safe_subject[:50]  # Limit length
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')

    filename = f"{timestamp}-{safe_subject}.md"
    filepath = INBOX_DIR / filename

    # Create note content
    content = f"""# Email: {email['subject']}

**From:** {email['from']}
**Date:** {email['date']}
**Status:** 🔴 Unprocessed

---

## Action Needed

- [ ] Read and respond
- [ ] Add to project if relevant
- [ ] Archive when done

---

## Email Content

{email['body']}

---

**Gmail ID:** {email['id']}
**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

**Tags:** #inbox #email #action-needed
"""

    filepath.write_text(content)
    return filename

def main():
    print("📧 Gmail → Obsidian Inbox Sync\n")

    try:
        service = get_gmail_service()
        emails = get_important_emails(service, max_results=5)

        if not emails:
            print("✅ No new important emails")
            return

        print(f"Found {len(emails)} important emails\n")

        for email in emails:
            filename = create_inbox_note(email)
            print(f"✅ Created: {filename}")
            print(f"   From: {email['from']}")
            print(f"   Subject: {email['subject']}\n")

        print(f"\n📥 Check your Obsidian Inbox folder ({len(emails)} new notes)")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
