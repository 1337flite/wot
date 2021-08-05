

import sys
import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)


client.create =('TestSheet3',1)
spreadsheet = client.open('TestSheet3')

worksheet = spreadsheet.add_worksheet("newsheet1",10,100)


theCsv = sys.argv[1]

#with open('data.csv', 'r') as file_obj:
with open(theCsv, 'r') as file_obj:
    content = file_obj.read()
    #client.import_csv(spreadsheet.id, data=content)
    client.import_csv(spreadsheet.id, data=content)




