#!/usr/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft21 Nov 2020
# A script to pull the number of battles a player has played in a clan wars season/campaign
# Usage:
# get_cw_battle_count.py <application_id> <clan_id> <season_id>



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

# Returns the number of battles of "battle_type" for the account "account_id"
# Valid battle_types are:
# random
# globalmap
# fort_battles - advances
# fort_sorties - skirms  - not sure how to tell the diff between T6 and T8 skirms
#
def get_battle_count(account_id,battle_type):
  battle_query = "https://worldoftanks.asia/wotup/profile/summary/?battle_type=" + battle_type + "&spa_id=" + account_id_str
  battle_res = requests.get(battle_query)
  battle_dict = json.loads(battle_res.text)
  battle_rating = battle_dict['data']['global_rating']
  if "None" == str(battle_rating):
    battle_count = 0
  else:
    battle_count = battle_dict['data']['battles_count']
  return battle_count

def get_battle_count_str(account_id,battle_type):
  return str(get_battle_count(account_id,battle_type))


application_id = '423670383adb5e0e08887a3e770c87c9'
clan_id = sys.argv[1]


region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu

#Get clan list of members
clan_details_url= region_api_server + "/wot/clans/info/?application_id=" + application_id + "&clan_id=" + str(clan_id)  + "&fields=members"

clan_details_res = requests.get(clan_details_url)
print clan_details_res
d = json.loads(clan_details_res.text)
member_list = d['data'][clan_id]['members']
member_list_len = len(member_list)

print "member,account_id,randoms,globalmap,advances,skirms"
for m in member_list:
  member_name = m['account_name']
  account_id = m['account_id']
  account_id_str = str(account_id)

  random_battles =  get_battle_count_str(account_id,"random")
  gm_battles =  get_battle_count_str(account_id,"globalmap")
  advances_battles =  get_battle_count_str(account_id,"fort_battles")
  skirm_battles =  get_battle_count_str(account_id,"fort_sorties")
  
  print member_name + ','+ account_id_str + ',' + random_battles  + ',' + gm_battles  + ',' + advances_battles   + ',' + skirm_battles
