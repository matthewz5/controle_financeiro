from src.def_config.config import CREDENTIALS_PATH, SPREADSHEET_ID

import pandas as pd

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

credentials = Credentials.from_service_account_file(CREDENTIALS_PATH)

service = build('sheets', 'v4', credentials=credentials)

def get_data(sheet_name):
    
    data = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=sheet_name).execute()

    values = data['values']

    data_output = pd.DataFrame(data['values'][1:], columns=data['values'][0])

    data_output = data_output.dropna(how='all')

    return data_output