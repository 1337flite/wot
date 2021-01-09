#!/Users/jtan/Documents/WoT/WoTAPI/venv_wot/bin/python
#  !/usr/bin/python


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
import requests
from operator import itemgetter
#Sheet: CW Season 15 - games per player 
#Sheet: Battles_played_Season_15_20201128


SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#COOKIES = dict(wgcwx_session_key='b96ebfbf0d235de9bb0a44724d44b6c7')
#COOKIES = dict(wgcwx_session_key='1RKzR1D1YfrEgFVazUAnxL_wVxRIbgZvtPrx2SpeZRu4')


pp = pprint.PrettyPrinter()

# Load creds
creds = ServiceAccountCredentials.from_json_keyfile_name('chook_creds.json', SCOPE)
#creds = ServiceAccountCredentials.from_json_keyfile_name('sabre_creds.json', SCOPE)

# Instantiate client object 
client = gspread.authorize(creds)

sheet_url1 =  "https://docs.google.com/spreadsheets/d/1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo/edit#gid=0"
sheet_url2 =  "https://docs.google.com/spreadsheets/d/1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo/"
sheet_key="1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo"

sheet1 = client.open('Provinces Test')
tab = sheet1.worksheet('provinces')
tab.update_cell(1,1,'hello')
sheet1.add_worksheet('new sheet1',100,100,0)
tab  = sheet1.worksheet('new sheet1')



batch = [{'range':'A1:F4','values':[[1,2,3,4,'FALSE','FALSE']] }]
tab.batch_update(batch)

#sheet = client.open(sheet_key)

# sheet1 is "funk" in cone's schedule.py
### sheet1 = client.open("TestSheet1").sheet1
#sheet1 = client.open("CW Season 15 - games per player").sheet1
#sheet1 = client.open_by_key('b96ebfbf0d235de9bb0a44724d44b6c7')
#open_by_key(key)
#creds.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')
#open_by_url
#gc.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')
#sheet1 = client.open_by_url('https://docs.google.com/spreadsheets/d/1UFRRIApyUwNgubmCwB5-4SBqLlgUXN8-ny8I3oiOeOM/').sheet1
#sheet1 = client.open_by_url('https://docs.google.com/spreadsheets/d/14o1lSzq7Snxk4REYPPBv_AQwfhXqGj3BaM8CvUnred4/').worksheet('Fame Point Tracker')
#'Fame Point Tracker'
#key='1ezzdo4Jvk3_V6xkJS8TdQq37bd5ycs8Zu73b4HJ8Xmc'
#sheet1 = client.open_by_key(key)

#creds.open_by_url(sheet_url2)
#result = sheet1.cell(1,1).value
#sheet1.update_cell(1,1,'new value2')
#sheet1.update_cell(2,1,'new cell 2,1')
#sheet1.update_cell(2,2,'new cell 2,2')
#sheet1.update_cell(3,1,'sabre creds')
#data = sheet1.row_values(1)
#data = sheet1.col_values(1)

#data = sheet1.get_all_records()
#data = sheet1.get_all_values()
#print "id " + str (sheet1.id)
#print "shit"
#print(data)
#print "pretty"
#pp.pprint(data)
