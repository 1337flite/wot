#!/usr/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft21 Nov 2020
# A script to pull the number of battles a player has played in a clan wars season/campaign
# Usage:
# get_cw_battle_count.py <application_id> <clan_id> <season_id>
import requests
import sys
import json



#clan_id=sys.argv[1]
#season_id = sys.argv[2]
#tier = sys.argv[3]
#application_id = "<ADD_YOUR_APP_ID>"
#clan_id="<ADD_CLAN_ID>"
#season_id="<ADD_SEASON_ID"
# Note there is no season 14 for Asia - presumably this was the season that was replaed with Seasos Advances.

application_id = sys.argv[1]
clan_id = sys.argv[2]
season_id = sys.argv[3]


region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu

#Get clan list of members
clan_details_url= region_api_server + "/wot/clans/info/?application_id=" + application_id + "&clan_id=" + str(clan_id)  + "&fields=members"

clan_details_res = requests.get(clan_details_url)

# create a dictionary from the string returned the the response
d = json.loads(clan_details_res.text)
clan_total_battles = 0

member_list = d['data'][clan_id]['members']
member_list_len = len(member_list)

print "player,account_id,battles"
for m in member_list:
  member_name = m['account_name']
  account_id = m['account_id']
  account_id_str = str(account_id)
  sbc_query =  region_api_server + "/wot/globalmap/seasonaccountinfo/?application_id=" + application_id  + "&season_id=" + season_id+ "&vehicle_level=10&account_id=" + str(account_id)
  sbc_res = requests.get(sbc_query)
  sbc_dict = json.loads(sbc_res.text)
  sbc_data_dict = sbc_dict['data']
  battle_count =  sbc_data_dict[account_id_str]['seasons'][season_id][0]['battles']
  if "None"  == str(battle_count):
    battle_count=0
  print member_name + "," + str(account_id) + "," + str(battle_count)
  clan_total_battles = clan_total_battles +  battle_count

print "Total,Clan," + str(clan_total_battles)
