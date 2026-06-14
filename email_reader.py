from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import base64

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]


def get_gmail_service():

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service


def extract_email_text(msg):

    payload = msg["payload"]

    if "parts" in payload:

        for part in payload["parts"]:

            if part["mimeType"] == "text/plain":

                data = part["body"].get("data")

                if data:

                    return base64.urlsafe_b64decode(
                        data
                    ).decode(
                        "utf-8",
                        errors="ignore"
                    )

    data = payload["body"].get("data")

    if data:

        return base64.urlsafe_b64decode(
            data
        ).decode(
            "utf-8",
            errors="ignore"
        )

    return None


def get_unread_emails():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        labelIds=["UNREAD"],
        maxResults=20
    ).execute()

    messages = results.get(
        "messages",
        []
    )

    emails = []

    for message in messages:

        msg = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="full"
        ).execute()

        email_text = extract_email_text(msg)

        if email_text:
            emails.append(
    {
        "id": message["id"],
        "body": email_text
    }
)

    return emails
def mark_as_read(message_id):

    service = get_gmail_service()

    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "removeLabelIds": [
                "UNREAD"
            ]
        }
    ).execute()