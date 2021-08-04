import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
import requests
from operator import itemgetter


SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
COOKIES = #see keepass gaming folder
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', SCOPE)
client = gspread.authorize(creds)

funk = client.open('S15 Spreadsheet') 
sheet = funk.worksheet("Battle Times")
monkey = client.open('Battle Times')
work = monkey.worksheet("Battle")
pp = pprint.PrettyPrinter()
previousJump = ''
previousTicks = []

def time2Jump(input):
    if input is None:
        return 'J?'
    firstSplit = input.split()
    if len(firstSplit) == 2:
        times = firstSplit[1].split(':')
    else:
        times = firstSplit[0].split(':')
    return 'J{}+{}'.format(int(times[0])-7, times[1])


def getBase(arenaName, baseNo):
    baseDict = {'Abbey': {1: 'South', 2: 'North'}, 'Cliff': {1: 'South', 2: 'North'}, 'Ensk': {1: 'North', 2: 'South'},
            "Fisherman's Bay": {1: 'North', 2: 'South'}, 'Fjords': {1: 'East', 2: 'West'}, 'Highway': {1: 'North', 2: 'South'},
            'Himmelsdorf': {1: 'South', 2: 'North'}, 'Karelia': {1: 'North', 2: 'South'}, 'Lakeville': {1: 'North', 2: 'South'},
            'Live Oaks': {1: 'South', 2: 'North'}, 'Malinovka': {1: 'South', 2: 'North'}, 'Mines': {1: 'South', 2: 'North'},
            'Murovanka': {1: 'North', 2: 'South'}, 'Overlord': {1: 'South', 2: 'North'}, 'Pilsen': {1: 'North', 2: 'South'},
            'Prokhorovka': {1: 'North', 2: 'South'}, 'Redshire': {1: 'South', 2: 'North'}, 'Ruinberg': {1: 'North', 2: 'South'},
            'Sand River': {1: 'East', 2: 'West'}, 'Serene Coast': {1: 'South', 2: 'North'}, 'Steppes': {1: 'South', 2: 'North'},
            'Westfield': {1: 'West', 2: 'East'}}

    return "{}-{}".format(baseNo, baseDict[arenaName][baseNo])


def prettyList(input, enemy=False):
    battle_time = input.get('battle_time')
    if battle_time:
        jump = time2Jump(input['battle_time'])
    else:
        jump = time2Jump(input['prime_time'])

    periphery = input.get('periphery')
    if periphery == 'W.o.T. Hong Kong':
        server = 'HK'
    elif periphery == 'W.o.T. Australia':
        server = 'ANZ'
    else:
        server = None

#    front = 'Basic' if input['front_id'] == "metal_wars_sg_league1" else 'Advanced'
    front = 'Basic' if input['front_id'] == "thunderstorm_sg_league1" else 'Advanced'
    arena = input['arena_name']

    roundNo = input.get('round_number')

    if arena == 'Serene Coast':
        arena = 'serene_coast'
    elif arena == 'Live Oaks':
        arena = 'live_oaks'
    elif arena == 'Cliff':
        arena = 'cliffs'
    elif arena == 'Prokhorovka':
        arena = 'phrokorovka'
    elif arena == "Fisherman's Bay":
        arena = 'fishermans_bay'
    elif arena == "Sand River":
        arena = 'sand_river'
    provinceMap = '=HYPERLINK("https://karellodewijk.github.io/maps/{}.jpg","{}")'.format(arena.lower(), input['arena_name'])
    if enemy is False:
        return [jump, input['province_name'], '', '', '', '', '', provinceMap, roundNo, server, front]
    else:
        clan = input['enemy']
        base = getBase(input['arena_name'], input['arena_resp_number'])
        return [jump, input['province_name'], clan['tag'], clan['elo_rating_10'], clan['arena_wins_percent'], clan['arena_battles_count'], base, provinceMap, roundNo, server, front]

while(True):
    nzTime = time.localtime(time.time())
    hour = int(time.strftime('%H', nzTime)) - 12
    funk = False
    while funk is False:
        battles = requests.get('https://asia.wargaming.net/globalmap/game_api/clan/2000010912/battles', cookies=COOKIES)
        try:
            battles = battles.json()
            funk = True
        except:
            print("Can't reach API")
            time.sleep(30)
    provinces = requests.get('https://api.worldoftanks.asia/wot/globalmap/clanprovinces/?application_id=3d63d9368fc5eba8cc8955ca2a70624a&clan_id=2000010912&language=en&fields=landing_type%2C+arena_name%2C+province_name%2C+front_id%2C+prime_time')
    provinces = provinces.json()
    provinces = provinces['data']['2000010912']
    #pp.pprint(battles)
    battleList = []
    for battle in battles['battles']:
        battleList.append(prettyList(battle, True))
    for battle in battles['planned_battles']:
        battleList.append(prettyList(battle))
    if provinces:
        for province in provinces:
            i = False
            prime = int(province['prime_time'].split(':')[0])
            if prime <= hour:
                continue
            for battle in battleList:
                if battle[1] == province['province_name']:
                    i = True
                    break
            if i is False:
                battleList.append(prettyList(province))

    battleList = sorted(battleList, key=itemgetter(0))
    originalList = sheet.get_all_values()
    originalList.pop(0)
    originalList.pop(0)

    finalList = []
    ticks = []
    firstLineFlag = False
    chosenFlag = False
    for battle in battleList:
        if battle[0] != previousJump:
            if firstLineFlag is True:
                finalList.append(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
            else:
                firstLineFlag = True
            previousJump = battle[0]
        for originalBattle in originalList:
            if battle[0] == originalBattle[0] and battle[1] == originalBattle[1]:
                ticks.append([originalBattle[11],originalBattle[12],originalBattle[13],originalBattle[14],originalBattle[15]])
                battle.extend([originalBattle[11],originalBattle[12],originalBattle[13],originalBattle[14],originalBattle[15]])
                finalList.append(battle)
                chosenFlag = True
                break
        if chosenFlag is False:
            battle.extend([False, False, False, False, True])
            finalList.append(battle)
        else:
            chosenFlag = False
    diff = len(originalList) - len(battleList)
    if diff > 0:
        for row in range(0,diff):
            finalList.append(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

    if len(finalList) != len(originalList) or ticks != previousTicks:
        batch = []
        row = 3
        for battle in finalList:
            namedRange = 'A{}:P{}'.format(row, row)
            batch.append({'range':namedRange, 'values':[battle]})
            row += 1
        try:
            sheet.batch_update(batch, value_input_option='USER_ENTERED')
            work.batch_update(batch, value_input_option='USER_ENTERED')
        except:
            print("couldn't reach google API, trying again in 1m")


    updateString = time.strftime('Last updated: %a %d/%m/%y at %H:%M:%S ACST', nzTime)
    try:
        sheet.update('A1',updateString)
        work.update('A1',updateString)
    except:
        print("couldn't reach google API, trying again in 1m")
    previousTicks = ticks
    time.sleep(60)

# https://www.youtube.com/watch?v=vISRn5qFrkM
# https://gspread.readthedocs.io/en/latest/api.html
