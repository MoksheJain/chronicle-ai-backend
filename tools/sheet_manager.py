import os
import json
import gspread
from google.oauth2.service_account import Credentials

def get_sheet():

    creds_dict = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

    credentials = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    client = gspread.authorize(credentials)

    sheet = client.open("ChronicleAI Subscribers").sheet1

    return sheet


def add_subscriber(email):

    sheet = get_sheet()
    sheet.append_row([email])


def get_all_subscribers():

    sheet = get_sheet()
    emails = sheet.col_values(1)[1:]  # skip header
    return emails
