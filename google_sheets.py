from service_account_setup import create_service
from google.oauth2 import service_account
import pandas as pd
from pprint import pprint



"""
To Do:

-Extract information from dictionary
-Figure out service account thing
"""

def get_google_form_data():
    SERVICE_SECRET_FILE = 'credentials\service_account_key.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SPREADSHEET_ID = '1XQeD4b6Hg0zqMpNuR5U9LcxZ80796P5QvZuW3E_xHAY'
    RANGE = "responses!A1:C999"
    service = create_service(API_NAME, API_VERSION, SCOPES, SERVICE_SECRET_FILE)
    result = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=RANGE, includeGridData=True).execute()

    update_order_row()
    with open('temp/current_amazon_order.txt', 'r') as f:
        order_row = int(f.readline())
    if len(result['sheets'][0]['data'][0]['rowData']) != order_row + 1:
        date = result['sheets'][0]['data'][0]['rowData'][order_row]['values'][0]['formattedValue']
        name = result['sheets'][0]['data'][0]['rowData'][order_row]['values'][1]['formattedValue']
        link = result['sheets'][0]['data'][0]['rowData'][order_row]['values'][2]['formattedValue']
        """
                            sheet?          ?             row          column
        """
        return date, name, link
    else:
        return None

    #print(f'The date is {date}. The name is {name}. The link is {link}')
    

def update_order_row():
    with open('temp/current_amazon_order.txt', 'r') as f:
        last_order_row = int(f.readline()) 
    current_order_row = last_order_row + 1
    with open('temp/current_amazon_order.txt', 'w') as f:
        f.write(str(current_order_row))