#!/usr/bin/python

import requests
import pprint
import sys
import json


pp = pprint.PrettyPrinter()

current_page=0
player_log_url='https://worldoftanks.asia/wotup/profile/global_map/front/history/?front_id=thunderstorm_bg&spa_id=2020855642&page=' + str(current_page) + '&language=en'

def getPlayerLogPage(thePage):
	player_log_url='https://worldoftanks.asia/wotup/profile/global_map/front/history/?front_id=thunderstorm_bg&spa_id=2020855642&page=' + str(thePage) + '&language=en'
	res=requests.get(player_log_url , {'authority':'worldoftanks.asia', 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'accept':'application/json, text/javascript, */*; q=0.01', 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua-mobile':'?0', 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36', 'sec-fetch-site':'same-origin', 'sec-fetch-mode':'cors', 'sec-fetch-dest':'empty', 'referer':'https://worldoftanks.asia/en/community/accounts/2020855642-chook_on_a_stick/?utm_campaign=wgcc&utm_medium=link&utm_source=clan_profile_military_personnel', 'accept-language':'en-US,en;q=0.9', 'cookie':'_ym_uid=1533974786322867895; csrftoken=CeV06aEKL4xngBGeboBbYmZSV6JN4w1f; cm.internal.bs_id=5631b261-1309-47fe-2819-9d9eae6b6e7e; uvt=1; cm.internal.spa_id=2020855642; cm.internal.realm=sg; _product_lvl=GA1.2.2035333793.1584172736; test_local_asia=GA1.2.1967885030.1584925567; _fbp=fb.1.1594537966271.1803943333; _rollupGa=GA1.2.985014759.1584046890; __atssc=google%3B3; prod_wgnet_lvl=GA1.2.1099938898.1533975822; _ga=GA1.1.1099938898.1533975822; _ym_d=1613277404; __atuvc=0%7C16%2C0%7C17%2C0%7C18%2C0%7C19%2C2%7C20; product_lvl=GA1.2.768437118.1622732283; wot_wgnet_lvl=GA1.2.768437118.1622732283; wgc-wot-portal=1; sessionid=ikw6m8d3qe5e4036hret4xiwwjhmuz2f; hlauth=1; WGAI="eyJsb2dpbm5hbWUiOiAiIiwgInRpbWVzdGFtcCI6IDE2MjcxODkyMTIsICJjbGFuX25hbWUiOiAiU0FCUkUtMSIsICJpc19zdGFmZiI6IGZhbHNlLCAiY2xhbl9iYW4iOiBudWxsLCAiZ2FtZV9iYW4iOiBudWxsLCAiY2xhbl90YWciOiAiU0FCUkUiLCAiY2xhbl9jb2xvciI6ICIjZGNjZDM5IiwgImhhc19mcmllbmRzIjogdHJ1ZSwgInNwYV9zdGF0ZSI6IG51bGwsICJuaWNrbmFtZSI6ICJjaG9va19vbl9hX3N0aWNrIiwgInNwYV9pZCI6IDIwMjA4NTU2NDIsICJoYXNfY2xhbm1hdGVzIjogdHJ1ZSwgImJhdHRsZXNfY291bnQiOiAyMzE1NSwgImNsYW5faWQiOiAyMDAwMDEwOTEyLCAiaXNfcHJlbWl1bV9hY3RpdmUiOiBmYWxzZX0="; hllang=en; cm.options.user_id=2020855642; cm.options.user_name=chook_on_a_stick; _gid=GA1.2.196059754.1627623416; product_lvl_gid=GA1.2.1960370372.1627623416; wot_wgnet_lvl_gid=GA1.2.1716258637.1627623416; _ym_isad=2; ref_domain=asia.wargaming.net; _ym_visorc=w; reg_ref_domain=asia.wargaming.net; newbie_lifetime=1533974850655-1627676069687; authentication_confirmation_expires_at=1627190062; _dc_gtm_UA-8323632-36=1; _dc_gtm_UA-40205758-4=1; _ga_281KMWX0KQ=GS1.1.1627675815.621.1.1627676070.59; _uetsid=271d76e0f0f811ebb36e17181abd7547; _uetvid=14f9ec907a8711ebb7197b4c86c2ada8; _gat_UA-150089307-6=1; _gat_UA-150089307-7=1; _gat_UA-150089307-8=1; _ga=GA1.2.1099938898.1533975822; _gat_UA-8323632-36=1; OptanonAlertBoxClosed=2021-07-30T20:14:31.956Z; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jul+31+2021+05%3A44%3A32+GMT%2B0930+(Australian+Central+Standard+Time)&version=6.15.0&hosts=&consentId=14ff6b5c-4314-46bd-8e9b-316846a8e377&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BSA'} )
	return json.loads(res.text)


#print res.text

data =  getPlayerLogPage(0)

#print data
page_size=data['data']['meta']['page_size']
pages_count=data['data']['meta']['pages_count']
current_page=data['data']['meta']['current_page']
#log_data=data['data']['data']
#print log_data 
#print "page_size: " + str(page_size) + " pages_count: " + str(pages_count) + " current_page: " + str(current_page)
#print
#print

log_data=[]

i=0
while i < pages_count:
	data = getPlayerLogPage(i)
	log_data.append(data['data']['data'])
	i=i+1
#	print "is is: " + str(i)


#pp.pprint(log_data)
print log_data

#pp.pprint(res.text)


