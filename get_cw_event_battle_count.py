#!/usr/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft21 Nov 2020
# A script to pull the number of battles a player has played in a clan wars season/campaign
# Usage:
# get_cw_battle_count.py <application_id> <clan_id> <season_id>
import requests
import sys
import json
import math


#clan_id=sys.argv[1]
#season_id = sys.argv[2]
#tier = sys.argv[3]
#application_id = "<ADD_YOUR_APP_ID>"
#clan_id="<ADD_CLAN_ID>"
#season_id="<ADD_SEASON_ID"
# Note there is no season 14 for Asia - presumably this was the season that was replaed with Seasos Advances.

argc = len(sys.argv) 
print "num args: " + str(argc)
application_id = sys.argv[1]
clan_id = sys.argv[2]
event_id = sys.argv[3]

if  argc >= 5:
  front_id = sys.argv[4]
#account_id = sys.argv[4]
gold = None

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

shares = dict()

#print "player,account_id,battles"

print"member_name,award_level,clan_rank,rank_delta,fame_points_to_improve_award,updated_at,battles,event_id,clan_id,rank,fame_points_since_turn,url,battles_to_award,fame_points,front_id"
for m in member_list:
  member_name = m['account_name']
  account_id = m['account_id']
  account_id_str = str(account_id)
  #sbc_query =  region_api_server + "/wot/globalmap/seasonaccountinfo/?application_id=" + application_id  + "&season_id=" + season_id+ "&vehicle_level=10&account_id=" + str(account_id)
  sbc_query =  region_api_server + '/wot/globalmap/eventaccountinfo/?event_id=' + event_id + '&account_id=' + str(account_id) + '&application_id=' + application_id 
  #+ '&front_id=' + front_id
  if  argc >= 5:
    sbc_query =  sbc_query + '&front_id=' + front_id
#  print sbc_query
  sbc_res = requests.get(sbc_query)
  sbc_dict = json.loads(sbc_res.text)
  sbc_data_dict = sbc_dict['data']
#  print sbc_data_dict
  event_data =  []
  event_data_array = sbc_data_dict[account_id_str]['events'][event_id]
#  print "event_data: "  
#  print event_data_array
  event_data_dict = event_data_array[0]
#  print "event_data_dict"
#  print event_data_dict
#  print
  award_level = str(event_data_dict['award_level'])
  account_id = str(event_data_dict['account_id'])
  clan_rank  = str(event_data_dict['clan_rank'])
  rank_delta = str(event_data_dict['rank_delta'])
  fame_points_to_improve_award = str(event_data_dict['fame_points_to_improve_award'])
  updated_at = str(event_data_dict['updated_at'])
  battles = str(event_data_dict['battles'])
  event_id = str(event_data_dict['event_id'])
  clan_id = str(event_data_dict['clan_id'])
  the_rank = str(event_data_dict['rank'])
  fame_points_since_turn = str(event_data_dict['fame_points_since_turn'])
  url = str(event_data_dict['url'])
  battles_to_award = str(event_data_dict['battles_to_award'])
  fame_points = str(event_data_dict['fame_points'])
  front_id  = str(event_data_dict['front_id'])
  print member_name + ',' + award_level + ',' + clan_rank + ',' + rank_delta + ',' + fame_points_to_improve_award  + ',' +  updated_at  + ',' +  battles + ',' + event_id  + ',' + clan_id + ',' + the_rank  + ',' + fame_points_since_turn  + ',' + url  + ',' + battles_to_award  + ',' + fame_points  + ',' + front_id


#print"member_name,award_level,clan_rank,rank_delta,fame_points_to_improve_award,updated_at,battles,event_id,clan_id,rank,fame_points_since_turn,url,battles_to_award,fame_points,front_id"

# {u'2006615108': 
#   {u'events': 
#     {u'metal_wars': 
#       [
#         {
#            u'award_level': None, 
#            u'account_id': 2006615108, 
#            u'clan_rank': 46, 
#            u'rank_delta': None, 
#            u'fame_points_to_improve_award': None, 
#            u'updated_at': None, 
#            u'battles': 2, 
#            u'event_id': u'metal_wars', 
#            u'clan_id': 2000010912, 
#            u'rank': None, 
#            u'fame_points_s1ince_turn': 140, 
#            u'url': None, 
#            u'battles_to_award': 0, 
#            u'fame_points': 140, 
#            u'front_id': 
#            u'metal_wars_bg'
#         }
#       ]
#     }
#    }
#  }



 
#  if "None"  == str(battle_count):
#    battle_count=0
#  print member_name + "," + str(account_id) + "," + str(battle_count)
#  shares[str(account_id)]={'account_name':member_name,'battles':battle_count,'share':None}
##  print shares 
#  clan_total_battles = clan_total_battles +  battle_count

#print "Total,Clan," + str(clan_total_battles)

