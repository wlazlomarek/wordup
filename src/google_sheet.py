from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

from dotenv import load_dotenv

load_dotenv()

# Create a Credentials object from the service account's credentials and the scopes your application needs access to.
SERVICE_ACCOUNT_FILE = 'google_secret_key/google_credential.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID of a sample spreadsheet.
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
service = build('sheets', 'v4', credentials=creds)


def read_google_sheet() -> dict:
    '''read_google_sheet [parse google sheet by ID]

    Returns:
        [dict]: [return dict {'dog': 'pies', ...}]
    '''
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range='sheet').execute()
    values = result.get('values', [])
    data = {el[0]: el[1] for el in values}
    return data


if __name__ == "__main__":
    data = read_google_sheet()
