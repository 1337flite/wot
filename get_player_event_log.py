#!/Users/jtan/Documents/WoT/WoTAPI/venv_p3/bin/python
# !/Users/jtan/Documents/WoT/WoTAPI/venv_p3/bin/python
# !/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# !/Users/jtan/Documents/WoT/WoTAPI/venv_wot/bin/python

import requests
import sys
import json
import math
import pprint
from datetime import datetime

# Event types:
# provinces
# battles
# events
# all
# forces

# Example URL
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=all&page_size=50000&page_number=1

region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu

clan_id = 2000010912
clan_id_str =  str (clan_id)
thePage_size = 50000
thePage_number = 0
theCategory = 'all'
# A list to add all the events to, so we have a single reversable data struct with all the events
theEvents  = []

debugLevel = 2



def debug(theLevel,theMessage):
  if (theLevel > debugLevel ):
    print (theMessage)

pp = pprint.PrettyPrinter()

#Get clan list of members
# params = of name/value pairs for the URL arguments
# headers = dict of name/value pairs for the request headers

clan_event_log_url = 'https://asia.wargaming.net/globalmap/game_api/clan/' + clan_id_str + '/log'
# 'https://worldoftanks.asia/wotup/profile/global_map/front/history/?front_id=renaissance_bg&spa_id=2020855642&page=8&page_size=500&language=en

theFront_id = 'renaissance_bg'
thePage =  0
theSpa_id = '2020855642'
theCounter = 0;
thePageStr = str (thePage)
theLanguage = 'en'
theSpa_id = sys.argv[1]
#print 'the SPA ID is: ' + str(theSpa_id)

theParams = {'front_id' : theFront_id, 'spa_id' : theSpa_id, 'page': thePageStr, 'language' : theLanguage}

theCookie = 'ym_uid=1533974786322867895; csrftoken=CeV06aEKL4xngBGeboBbYmZSV6JN4w1f; common_menu_ga=GA1.2.1319259780.1533974851; cm.internal.bs_id=5631b261-1309-47fe-2819-9d9eae6b6e7e; uvt=1; cm.internal.spa_id=2020855642; cm.internal.realm=sg; tmr_lvid=38cdaabf23829613ff6c1cf6eaa165c7; tmr_lvidTS=1570433830809; _product_lvl=GA1.2.2035333793.1584172736; test_local_asia=GA1.2.1967885030.1584925567; _fbp=fb.1.1594537966271.1803943333; _rollupGa=GA1.2.985014759.1584046890; tmr_reqNum=337; _ym_d=1597456406; wgc-wot-portal=1; _gcl_au=1.1.1112143448.1605266009; mpvid=1; __atssc=google%3B3; __atuvc=0%7C49%2C0%7C50%2C0%7C1%2C0%7C1%2C4%7C53; sessionid=xog6dfpetqr9k7au7cbxglp924tzrbyi; prod_wgnet_lvl=GA1.2.1099938898.1533975822; _uetvid=09fee6a048fe11eb998bff95a2fcb6ec; hlauth=1; hllang=en; _ga=GA1.1.1099938898.1533975822; product_lvl=GA1.2.730638115.1533974793; wot_wgnet_lvl=GA1.2.730638115.1533974793; cm.options.user_id=2020855642; cm.options.user_name=chook_on_a_stick; _gid=GA1.2.997930519.1611135450; product_lvl_gid=GA1.2.997930519.1611135450; wot_wgnet_lvl_gid=GA1.2.997930519.1611135450; _ym_isad=2; _ym_visorc=w; newbie_lifetime=1533974850655-1611385423257; authentication_confirmation_expires_at=1610700284; _ga_281KMWX0KQ=GS1.1.1611385095.335.1.1611385680.60; _ga=GA1.1.1099938898.1533975822'

theHeaders = {'authority':'asia.wargaming.net', 'sec-ch-ua':'"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"', 'x-csrf-token':'b3dceb3b-1805-4d06-ae27-a0b99f46df3e', 'sec-ch-ua-mobile':'?0', 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 'content-type':'application/json', 'accept':'*/*', 'sec-fetch-site':'same-origin', 'sec-fetch-mode':'cors', 'sec-fetch-dest':'empty', 'referer':'https://asia.wargaming.net/globalmap/', 'accept-language':'en-US,en;q=0.9','cookie':theCookie}

player_history_log_url = 'https://worldoftanks.asia/wotup/profile/global_map/front/history/'

#res = req = requests.get(player_history_log_url,headers = theHeaders , params =  theParams)

#theJson = json.loads(res.text)
#pp.pprint(theJson)


#current_page = theJson['data']['meta']['current_page']
#page_count = theJson['data']['meta']['page_count']


# Returna  page of a players history data
def getPlayerHistoryPage(thePlayerId,thePageNum):
  debug(2,"Fetching page: " + str(thePageNum) + " for SPAID: " + str(theSpa_id ))
  theParams = {'front_id' : theFront_id, 'spa_id' : thePlayerId , 'page': thePageNum, 'language' : theLanguage}
  res = req = requests.get(player_history_log_url,headers = theHeaders , params =  theParams)
  theJson = json.loads(res.text)
  return theJson['data']

def getPlayerHistoryPageData(thePlayerId,thePageNum):
  someJson = getPlayerHistoryPage(thePlayerId,thePageNum)
  return someJson['data']

def getPlayerHistoryPageMeta(thePlayerId,thePageNum):
  someJson = getPlayerHistoryPage(thePlayerId,thePageNum)
  return someJson['meta']

# Returns the number of pages of history data available for a player
def getPlayerHistoryNumPages(thePlayerId):
  someJson = getPlayerHistoryPage(thePlayerId,0)
  debug(2,'Fetching num history pages for SPAID: ' + str(thePlayerId))
  return someJson['meta']['pages_count']
  #pp.pprint(someJson['meta'])


# u'type': u'Participating in battle'}
# u'type': u'Spent on personal bonuses'}

def printPlayerHistoryRecordCsv(theRecord):
  #pp.pprint(theRecord)
  comma = ','
  won = 0
  spent = 0    
  createdAt = theRecord['created_at']
  event = theRecord['event_id']
  fpDelta = theRecord['fame_points_delta']
  fpTotal = theRecord['fame_points_total']
  front = theRecord['front']
  province = theRecord['province']
  spaId = theRecord['spa_id']
  type = theRecord['type']

  theDateTime = datetime.strptime(createdAt,'%Y-%m-%dT%H:%M:%S%z')
  epochTime = theDateTime.timestamp()
  localtime = datetime.fromtimestamp(epochTime)
  localTimeStr = localtime.strftime('%Y-%m-%d,%H:%M:%S')
 
  if fpDelta < 0 :
    spent = fpDelta
  else:
    won = fpDelta
  print (localTimeStr + comma + str(spent) + comma + str(won) + comma + type) 
  #print (createdAt + comma + localTimeStr + comma + str(spent) + comma + str(won) + comma + str(fpDelta) + comma + str(fpTotal) + comma  + str(spaId) + comma + type)



numPages = getPlayerHistoryNumPages(theSpa_id)
#debug(1,theSpa_id + ' has ' + str(numPages) + ' pages of history')

while (theCounter < numPages+1):
  thePageData = getPlayerHistoryPageData(theSpa_id,theCounter)
  for record in thePageData:
    theEvents.append(record)

  #  printPlayerHistoryRecordCsv(record)
  theCounter = theCounter +1
theEvents.reverse()

for event in theEvents:
  printPlayerHistoryRecordCsv(event)

#{u'created_at': u'2021-01-11T08:48:37+0000',
# u'event_id': u'renaissance',
# u'fame_points_delta': 94,
# u'fame_points_total': 136,
# u'front': {u'id': u'renaissance_bg', u'name': u'Renaissance', u'url': u''},
# u'province': {u'id': u'zhytkavichy', u'name': u'Zhytkavichy'},
# u'spa_id': 2020855642,
# u'type': u'Participating in battle'}
#{u'created_at': u'2021-01-11T08:26:59+0000',
# u'event_id': u'renaissance',
# u'fame_points_delta': -50,
# u'fame_points_total': 42,
# u'front': {u'id': u'renaissance_bg', u'name': u'Renaissance', u'url': u''},
# u'province': None,
# u'spa_id': 2020855642,
# u'type': u'Spent on personal bonuses'}
