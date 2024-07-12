import imaplib
import email
from email.header import decode_header
import caldav
import os 


# import json
# credentials = json.load(open('../email_credentials.json'))
credentials = dict(os.environ)

mail = imaplib.IMAP4_SSL(credentials['imap_host'])
mail.login(credentials['email_user'], credentials['email_pass'])

# Select the inbox
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, 'ALL')
email_ids = messages[0].split()

# print(messages)

# Connect to the CalDAV server
client = caldav.DAVClient(url=credentials['caldav_url'], username=credentials['email_user'], password=credentials['email_pass'])

principal = client.principal()
calendars = principal.calendars()

# print(messages,calendars)

if not calendars:
    print("No calendars found")
    exit()

calendar = calendars[0]  # Use the first calendar found

user = {}

for email_id in email_ids:
    # Fetch the email by ID
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            email_subject = decode_header(msg["Subject"])[0][0]
            if isinstance(email_subject, bytes):
                email_subject = email_subject.decode()
                
            email_from = msg.get("From")
            sender_name, sender_email = email.utils.parseaddr(email_from)
            user[sender_email] = sender_name

            # Check if the email has a meeting invite (iCalendar format)
            for part in msg.walk():
                if part.get_content_type() == "text/calendar":
                    ical_content = part.get_payload(decode=True).decode()

                    # Add the event to the CalDAV calendar
                    try:
                        event = calendar.add_event(ical_content)
                        # print(f"Added event from email ID: {str(email_id)}: {email_subject}")
                    except Exception as e:
                        # print('skipping',email_subject)
                        ...


# Logout from the IMAP server
mail.logout()

