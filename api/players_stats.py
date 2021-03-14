import requests
import json
import creds

team_id = { 1:'Atlants Hawks', 2:'Boston Celtics', 4:'Brooklyn Nets', 5:'Charlotte Hornet', 
             6:'Chicago Bulls', 7:'Cleveland Cavaliers', 8:'Dallas Mavericks', 
             9:'Denver Nuggets', 10:'Detroit Pistons', 11:'Golden State Warriors', 
             14:'Houston Rockets', 15:'Indiana Pacers', 16:'LA Clippers', 17:'LA Lakers', 
             19:'Memphis Grizzlies', 20:'Miami Heat', 21:'Milwaukee Bucks', 22:'Minnesota Timberwolves',
             23:'New Orleans Pelicans', 24:'New York Knicks', 25:'Oklahoma City Thunder', 
             26:'Orlanda Magic', 27:'Philadelphia 76ers', 28:'Pheonix Suns', 29:'Portland Trail Blazers', 
             30:'Sacramento Kings', 31:'San Antonio Spurs', 38:'Toronto Raptors', 
             40:'Utah Jazz', 41:'Washington Wizards'}
            
def getPlayerStats(playerName):
    playerName = playerName.lower()
    f = open('./data/players.json')
    playerDict = json.load(f)
    playerID =  playerDict[playerName]

    f = open('./data/validGames.json')
    validGameIDsList = json.load(f)
    validGameIDs = set(validGameIDsList)

    f = open('./data/gameDateInfo.json')
    gameDates = json.load(f)

    url = "https://api-nba-v1.p.rapidapi.com/statistics/players/playerId/" + str(playerID)

    headers = {
        'x-rapidapi-key': "<< ACCESS TOKEN >>",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers).json()
    results = response['api']['statistics']
    points = {}

    points=[]
    totalP=0
    rebounds=[]
    totalR=0
    assists=[]
    totalA=0
    ft=[]
    totalFT=0
    labels=[]

    for i in range(len(results)):
        game = results[i]
        gameId = game['gameId']
        if(str(gameId) not in validGameIDsList): continue
        points.append(game['points'])
        if(game['points'] != ''): totalP = totalP + int(game['points'])
        rebounds.append(game['totReb'])
        if(game['totReb'] != ''): totalR = totalR + int(game['totReb'])
        assists.append(game['assists'])
        if(game['assists'] != ''): totalA = totalA + int(game['assists'])
        ft.append(game['ftm'])
        if(game['ftm'] != ''): totalFT = totalFT + int(game['ftm'])
        labels.append(gameDates[gameId])
        

    return points, rebounds, assists, ft, labels, totalP, totalA, totalR, totalFT
    

def getPlayerInfo(playerName):
    playerName = playerName.lower()
    f = open('./data/playersBioInfo.json')
    playerDict = json.load(f)
    playerBioInfo =  playerDict[playerName]


    team = playerBioInfo['team']
    school = playerBioInfo['college']
    dob = playerBioInfo['dob']
    height = playerBioInfo['height']
    weight = playerBioInfo['weight']

    tempDict = {}
    tempDict['team'] = team
    tempDict['college'] = school
    tempDict['dob'] = dob
    tempDict['height'] = height
    tempDict['weight'] = weight

    return tempDict

def getPlayerNames():
    f = open('./data/playerNames.json')
    playersDict = json.load(f)
    players = []
    for player in playersDict:
        players.append(player)

    return players
