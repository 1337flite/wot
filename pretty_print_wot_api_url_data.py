#!/usr/bin/python
# Author: chook_on_a_stick asia server
# Intitial Draft 8 JAN 2021
# A script to pull data from a Wg WoT API/Site URL and pretty print the metadata and data.
# Usage:
# pretty_print_wot_api_url_data.py <url>
#  E.g. pretty_print_wot_api_url_data.py https://api.worldoftanks.asia/wot/globalmap/provinces/?application_id=423670383adb5e0e08887a3e770c87c9&front_id=renaissance_sg_league2


import requests
import sys
import json
import math
import pprint

application_id = '423670383adb5e0e08887a3e770c87c9'
target_url = sys.argv[1]

region_api_server="https://api.worldoftanks.asia"
# Asia https://api.worldoftanks.asia
# NA https://api.worldoftanks.com
# RU https://api.worldoftanks.eu
# EU https://api.worldoftanks.eu




res = requests.get(target_url)
d = json.loads(res.text)

meta_data = d['meta']
data = d['data']

pp = pprint.PrettyPrinter()
#print event_data
print "#Meta Data"
pp.pprint(meta_data)
print "\n"
print "#Data"
pp.pprint(data)

