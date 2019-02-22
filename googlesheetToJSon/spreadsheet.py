import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('mencobaGoogleSpreadSheet-4f1e21a5cd3c.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("GGD_DataBor").sheet5