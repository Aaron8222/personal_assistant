from google_setup import Create_Service
import pandas as pd
from pprint import pprint
import time


def get_google_form_data():
    CLIENT_SECRET_FILE = 'credentials\credentials.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SPREADSHEET_ID = '1_0qA495FduawJtjFzPa0rylCIpZWbVZTH0SnDoXEK-4'
    RANGE = "responses!A1:C2"


    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    result = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()
    #rows = result.get('values', [])
    pprint(result)

get_google_form_data()