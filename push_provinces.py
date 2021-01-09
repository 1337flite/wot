#!/Users/jtan/Documents/WoT/WoTAPI/venv_wot/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft21 Nov 2020
# A script to pull the number of battles a player has played in a clan wars season/campaign
# Usage:
# get_provinces.py <application_id> <front_id>

#https://api.worldoftanks.asia/wot/globalmap/provinces/?application_id=423670383adb5e0e08887a3e770c87c9&front_id=season_15_sg_tier10_15x15

# This is how you pull account GM battles spa_id is the account id
# https://worldoftanks.asia/wotup/profile/summary/?spa_id=2020855642&battle_type=globalmap
#
# Returns something like:
# {"status": "ok", "data": {"battles_count": 438, "damage_dealt": 241374, "frags_max": 3, "global_rating": 3504, "xp_amount": 105619, "wins_count": 131, "xp_max": 1431, "hits_count": 1202, "shots_count": 1855, "wins_ratio": 29.91, "xp_per_battle_average": 241, "hits_ratio": 64.8, "damage_per_battle_average": 551, "mastery": {"vehicles_count": 239, "mastery_count": 23}}}
#
# EXXCEPT PLAYERS WITH NO GM BATTLES they return something like this:
# {"status": "ok", "data": {"global_rating": null, "wins_ratio": null, "xp_per_battle_average": null, "hits_ratio": null, "damage_per_battle_average": null, "mastery": {"vehicles_count": 146, "mastery_count": 20}}}
# landing_types: 'null' 'tournament' 'tournament'
import requests
import sys
import json
import math
import pprint
import gspread
import datetime

now =  datetime.datetime.now()
#now =  datetime.datetime(2021,01,10)
today_str = now.strftime('%Y-%m-%d')
year_str = now.strftime('%Y')
month_str = now.strftime('%m')
day_str = now.strftime('%d')
print 'today_str: ' + today_str

# Load creds
creds = ServiceAccountCredentials.from_json_keyfile_name('chook_creds.json', SCOPE)
#creds = ServiceAccountCredentials.from_json_keyfile_name('sabre_creds.json', SCOPE)

# Instantiate client object
client = gspread.authorize(creds)

#sheet_url1 =  "https://docs.google.com/spreadsheets/d/1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo/edit#gid=0"
#sheet_url2 =  "https://docs.google.com/spreadsheets/d/1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo/"
#sheet_key="1q7OLH8qK0KAgWA882nZ7UOtm0vGM7Q8RL41xxWLFcYo"

sheet1 = client.open('Provinces Test')
tab = sheet1.worksheet('provinces')
#tab.update_cell(1,1,'hello')

batch = [{'range':'A1:F4','values':[[1,2,3,4,'FALSE','FALSE']] }]
tab.batch_update(batch)

#sheet1.add_worksheet('new sheet',100,100,0)


pp = pprint.PrettyPrinter()
application_id = '423670383adb5e0e08887a3e770c87c9'
front_id = sys.argv[1]

print "front_id: " + front_id

region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu


#Get clan list of members
# https://api.worldoftanks.asia/wot/globalmap/provinces/?application_id=423670383adb5e0e08887a3e770c87c9&front_id=season_15_sg_tier10_15x15
# https://api.worldoftanks.asia/wot/globalmap/provinces/?application_id=423670383adb5e0e08887a3e770c87c9&front_id=season_15_sg_tier10_15x15
front_details_url= region_api_server + "/wot/globalmap/provinces/?application_id=" + application_id + "&front_id=" + front_id

front_details_res = requests.get(front_details_url)
#print clan_details_res
d = json.loads(front_details_res.text)
print "length of data: " + str(len(d))

status=d['status']
metadata=d['meta']
data = d['data']

#pp.pprint(data)

province_data = d['data']
print d.keys()
#plen = len(province_data)
#print "plen: " + str(plen)



# J1 08:00:00
# J1_15 08:15:00
# J2 09:00:00
# J2_15 09:15:00
# J3 10:00:00
# J3_15 10:15:00
# J4 11:00:00
# J4_15 11:15:00
# J5 12:00:00
# J5_15 12:15:00
# J6 13:00:00
# J6_15 13:15:00
# J7 14:00:00
# J7_15 14:15:00


j1 = []
j115 = []
j2 = []
j215 = []
j3 = []
j315 = []
j4 = []
j415 = []
j5 = []
j515 = []
j6 = []
j615 = []
j7 = []
j715 = []

jumps = [ j1,j115,j2,j215,j3,j315,j4,j415,j5,j515,j6,j615,j7,j715]


def getJumpFromTime(time):
  if time == '08:00:00':
    return 'J1'
  if time == '08:15:00':
    return 'J1+15'
  if time == '09:00:00':
    return 'J2'
  if time == '09:15:00':
    return 'J2+15'
  if time == '10:00:00':
    return 'J3'
  if time == '10:15:00':
    return 'J3+15'
  if time == '11:00:00':
    return 'J4'
  if time == '11:15:00':
    return 'J4+15'
  if time == '12:00:00':
    return 'J5'
  if time == '12:15:00':
    return 'J5+15'
  if time == '13:00:00':
    return 'J6'
  if time == '13:15:00':
    return 'J6+15'
  if time == '14:00:00':
    return 'J7'
  if time == '14:15:00':
    return 'J7+15'
  return 'none'
 

jumps_by_time ={ '08:00:00':j1, '08:15:00':j115, '09:00:00':j2, '09:15:00':j215, '10:00:00':j3, '10:15:00':j315, '11:00:00':j4, '11:15:00':j415, '12:00:00':j5, '12:15:00':j515, '13:00:00':j6, '13:15:00':j615, '14:00:00':j7, '14:15:00':j715 } 

print "#province,map,max_bets,current_min_bet,last_won_bet,landing_type,battles_start_at"
for province in province_data:
  active_battles = province['active_battles']
  status = province['status']
  front_name = province['front_name']
  max_bets = province['max_bets']
  arena_name = province['arena_name']
  attackers = province['attackers']
  neighbours = province['neighbours']
  last_won_bet = province['last_won_bet']
  province_name = province['province_name']
  is_borders_disabled = province['is_borders_disabled']
  arena_id = province['arena_id']
  prime_time = province['prime_time']
  current_min_bet = province['current_min_bet']
  battles_start_at = province['battles_start_at']
  pillage_end_at = province['pillage_end_at']
  world_redivision = province['world_redivision']
  province_id = province['province_id']
  landing_type = province['landing_type']
  owner_clan_id = province['owner_clan_id']
  revenue_level = province['revenue_level']
  daily_revenue = province['daily_revenue']
  uri = province['uri']
  server = province['server']
  competitors = province['competitors']
  round_number = province['round_number']
  front_id = province['front_id']
  
  #pp.pprint(province)
  time_date = battles_start_at.split('T')
  the_date = time_date[0]
  the_time = time_date[1]
  the_jump = getJumpFromTime(the_time)
  # D has 11 fields  cols A-K
  d = {'province_id':province_id,'arena_id':arena_id,'max_bets':max_bets,'current_min_bet':current_min_bet,'last_won_bet':last_won_bet,'landing_type':landing_type,'battles_start_at':battles_start_at,'the_date':the_date,'the_time':the_time,'the_jump':the_jump}
  #print "the jump time is: " + the_time 
  jumps_by_time[the_time].append(d)
  #pp.pprint(jumps_by_time[the_time])

#for j in jumps:
#  j_len=len(j)
#  print "j is " + str(j_len)
#  print j 




#print "j1\n"

#pp.pprint(jumps[0])
#print "j115\n\n\n"
#pp.pprint(jumps[1])


#print jump['province_id']
#print jump['arena_id']
#print jump['max_bets']
#print jump['current_min_bet']
#print jump['last_won_bet']
#print jump['landing_type']
#print jump['battles_start_at']
#print jump['the_date']
#print jump['the_time']






#  print jump['province_id']
#  print jump['arena_id']
#  print jump['max_bets']
#  print jump['current_min_bet']
#  print jump['last_won_bet']
#  print jump['landing_type']
#  print jump['battles_start_at']
#  print jump['the_date']
#  print jump['the_time']
#for j in j1:
print "#J1"
print "#province,map,max_bets,current_min_bet,last_won_bet,landing_type,datetime,date,time,jump"
for jump in jumps_by_time['08:00:00']:
#  pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

print "J1+15"
for jump in jumps_by_time['08:15:00']:
#  pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
 
print "J2"
for jump in jumps_by_time['09:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J2+15"
for jump in jumps_by_time['09:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J3"
for jump in jumps_by_time['10:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J3+15"
for jump in jumps_by_time['10:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

print "J4"
for jump in jumps_by_time['11:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J4+15"
for jump in jumps_by_time['11:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

print "J5"
for jump in jumps_by_time['12:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J5+15"
for jump in jumps_by_time['12:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

print "J6"
for jump in jumps_by_time['13:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J6+15"
for jump in jumps_by_time['13:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

print "J7"
for jump in jumps_by_time['14:00:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']
print "J7+15"
for jump in jumps_by_time['14:15:00']:
  #pp.pprint(jump)
  print jump['province_id']+ "," + jump['arena_id']+ "," + str(jump['max_bets']) + "," + str(jump['current_min_bet'])+ "," + str(jump['last_won_bet']) + "," + str(jump['landing_type']) + "," + jump['battles_start_at'] + "," + jump['the_date'] + "," + jump['the_time'] + "," + jump['the_jump']

#  print  province_id + "," + arena_id + "," + str(max_bets) + "," + str(current_min_bet) + "," + str(last_won_bet) + "," + str(landing_type) + "," + battles_start_at + "," + the_date + "," + the_time
#  print "province: " + province_id + ",map: " + arena_id + ",max_bets: " + str(max_bets) + ",current_min_bet: " + str(current_min_bet) + ",last_won_bet: " + str(last_won_bet) + ",landing_type: " + str(landing_type) + ",battles_start_at: " + battles_start_at
#  print "\n\n\n"


#print "\n----\nJ1"
#pp.pprint(j1)
#
#print "\n----\nJ1+15"
#pp.pprint(j115)
#
#print "\n----\nj2"
#pp.pprint(j2)
#
#print "\n----\nJ2+15"
#pp.pprint(j215)
#
#print "\n----\nJ3"
#pp.pprint(j2)
#
#print "\n----\nJ3+15"
#pp.pprint(j315)



# 08:00:00
# 08:15:00
# 09:00:00
# 09:15:00
# 10:00:00
# 10:15:00
# 11:00:00
# 11:15:00
# 12:00:00
# 12:15:00
# 13:00:00
# 13:15:00
# 14:00:00
# 14:15:00

#{u'active_battles': [],
# u'arena_id': u'23_westfeld',
# u'arena_name': u'\u0e40\u0e27\u0e2a\u0e15\u0e4c\u0e1f\u0e34\u0e25\u0e14\u0e4c',
# u'attackers': [],
# u'battles_start_at': u'2021-01-08T10:00:00',
# u'competitors': [],
# u'current_min_bet': 100,
# u'daily_revenue': 0,
# u'front_id': u'renaissance_sg_league2',
# u'front_name': u'renaissance_sg_league2',
# u'is_borders_disabled': False,
# u'landing_type': None,
# u'last_won_bet': 0,
# u'max_bets': 1,
# u'neighbours': [u'calatayud', u'castellondelaplana', u'lleida', u'saragossa'],
# u'owner_clan_id': None,
# u'pillage_end_at': None,
# u'prime_time': u'10:00',
# u'province_id': u'vinaros',
# u'province_name': u'\u0e27\u0e34\u0e19\u0e32\u0e23\u0e2d\u0e2a',
# u'revenue_level': 0,
# u'round_number': None,
# u'server': u'502',
# u'status': None,
# u'uri': u'/#province/vinaros',
# u'world_redivision': False}
