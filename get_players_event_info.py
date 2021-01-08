#!/usr/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft21 Nov 2020
# A script to pull the event (Personal Reward Campaign) data for all the players in a clan
# Usage:
# get_players_event_info.py <clan_id> <event_id> <front_ud>
# E.g. get_players_event_info.py 2000010912  metal_wars metal_wars_bg



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

application_id = '423670383adb5e0e08887a3e770c87c9'
clan_id = sys.argv[1]
event_id = sys.argv[2]
front_id = sys.argv[3]


region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu

#Get clan list of members
clan_details_url= region_api_server + "/wot/clans/info/?application_id=" + application_id + "&clan_id=" + str(clan_id)  + "&fields=members,tag"

clan_details_res = requests.get(clan_details_url)
d = json.loads(clan_details_res.text)

pp = pprint.PrettyPrinter()

clan_tag = d['data'][clan_id]['tag']
member_list = d['data'][clan_id]['members']
member_list_len = len(member_list)
print "#" + clan_tag
print "clan_tag,account_name,account_id,award_level,battles,battles_to_award,clan_id,clan_rank,event_id,fame_points,fame_points_since_turn,fame_points_to_improve_award,front_id,rank,rank_delta,updated_at,url"
for m in member_list:
  member_name = m['account_name']
  account_id = m['account_id']
  account_id_str = str(account_id)



  account_event_info_url = region_api_server + "/wot/globalmap/eventaccountinfo/?application_id=" + application_id + "&clan_id=" + str(clan_id)  + '&event_id=' +event_id + '&front_id=' +front_id 
  acc_event_info_res = requests.get(account_event_info_url)
  acct_event_info = json.loads(acc_event_info_res.text)
  acct_event_data = acct_event_info['data'][account_id_str]['events'][event_id][0]
#  pp.pprint(acct_event_data)

  award_level = acct_event_data['award_level']
  battles = acct_event_data['battles']
  battles_to_award = acct_event_data['battles_to_award']
  clan_id = acct_event_data['clan_id']
  clan_rank = acct_event_data['clan_rank']
  event_id = acct_event_data['event_id']
  fame_points = acct_event_data['fame_points']
  fame_points_since_turn = acct_event_data['fame_points_since_turn']
  fame_points_to_improve_award = acct_event_data['fame_points_to_improve_award']
  front_id = acct_event_data['front_id']
  rank = acct_event_data['rank']
  rank_delta = acct_event_data['rank_delta']
  updated_at = acct_event_data['updated_at']
  url = acct_event_data['url']

  print clan_tag + ',' + member_name + ',' + account_id_str + ',' + str(award_level) + ',' + str(battles) + ',' + str(battles_to_award) + ',' + str(clan_id) + ',' + str(clan_rank) + ',' + event_id + ',' + str(fame_points) + ',' + str(fame_points_since_turn) + ',' + str(fame_points_to_improve_award) + ',' + front_id + ',' + str(rank) + ',' + str(rank_delta) + ',' + str(updated_at) + ',' + str(url)



