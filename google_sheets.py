from service_account_setup import Create_Service
from google.oauth2 import service_account
import pandas as pd
from pprint import pprint


def get_google_form_data():
    SERVICE_SECRET_FILE = 'credentials\client_key.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SPREADSHEET_ID = '1QGyBmp2lxFNSkTHnPbuRAvtpNP4-wmwkSc06zbsQ75Y'
    RANGE = "responses!A1:C2"

    service = Create_Service(SERVICE_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    result = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=RANGE, includeGridData=True).execute()
    pprint(result)

get_google_form_data()