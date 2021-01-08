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

import requests
import sys
import json
import math
import pprint


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
province_data = d['data']
#pp.pprint(province_data)
plen = len(province_data)
print "plen: " + str(plen)

#p = province_data[10]
#print p['arena_id']
pp.pprint(front_details_res.text)

#clan_tag = d['data'][clan_id]['tag']
#member_list = d['data'][clan_id]['members']
#member_list_len = len(member_list)
#print "#" + clan_tag
#print "member,account_id,randoms,globalmap,advances,skirms"
#for m in member_list:
#  member_name = m['account_name']
#  account_id = m['account_id']
#  account_id_str = str(account_id)
#
#  random_battles =  get_battle_count_str(account_id,"random")
#  gm_battles =  get_battle_count_str(account_id,"globalmap")
#  advances_battles =  get_battle_count_str(account_id,"fort_battles")
#  skirm_battles =  get_battle_count_str(account_id,"fort_sorties")
#  
#/usr/bin/python  print member_name + ','+ account_id_str + ',' + random_battles  + ',' + gm_battles  + ',' + advances_battles   + ',' + skirm_battles
