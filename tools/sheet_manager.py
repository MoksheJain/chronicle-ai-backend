import os
import json
import gspread
from google.oauth2.service_account import Credentials

def get_sheet():

    creds_raw = os.getenv("GOOGLE_CREDENTIALS")

    if not creds_raw:
        raise Exception("GOOGLE_CREDENTIALS not found in environment variables")

    creds_dict = json.loads(creds_raw)

    # 🔥 Fix newline formatting issue
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

    credentials = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    client = gspread.authorize(credentials)

    sheet = client.open_by_key(
        "16mc8lBDL-6qEVXvkAC62ArKdSkZPlGOd52lq2dbnVLA"
    ).sheet1

    return sheet


def add_subscriber(email):

    sheet = get_sheet()
    sheet.append_row([email])


def get_all_subscribers():

    sheet = get_sheet()
    emails = sheet.col_values(1)[1:]  # skip header
    return emails
