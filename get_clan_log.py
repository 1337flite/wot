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



# All Events
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=all&page_size=30&page_number=1
# Divisions
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=forces&page_size=30&page_number=1
# Battles
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=battles&page_size=30&page_number=1
# Provinces
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=provinces&page_size=30&page_number=1
# Events
# https://asia.wargaming.net/globalmap/game_api/clan/2000010912/log?category=events&page_size=30&page_number=1



import requests
import sys
import json
import math
import pprint

application_id = '423670383adb5e0e08887a3e770c87c9'
clan_id = sys.argv[1]
log_type = sys.argv[2]
page_size = sys.argv[3]

#event_id = sys.argv[2]
#front_id = sys.argv[3]


page_size_str = str (page_size)
clan_id_str = str(clan_id)
page_number_str = str(1)

region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu



asia_clan_log_url = "https://asia.wargaming.net/globalmap/game_api/clan/" + clan_id_str + " /log?category=" + log_type + "&page_size=" + page_size_str + "&page_number=" + page_number_str
print "asia_clan_log_url: " + asia_clan_log_url
#Get clan list of members
#clan_details_url= region_api_server + "/wot/clans/info/?application_id=" + application_id + "&clan_id=" + str(clan_id)  + "&fields=members,tag"

clan_log_res = requests.get(asia_clan_log_url)
d = json.loads(clan_log_res.text)

event_data = d['data']

pp = pprint.PrettyPrinter()

pp.pprint(event_data)

