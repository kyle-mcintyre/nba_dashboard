import json
import requests
import time
from datetime import datetime
from dateutil import tz
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

allPlayers = ["Ivica Zubac", "Cody Zeller", "Trae Young", "Thaddeus Young", "Delon Wright", "Robert Woodard II", "Christian Wood", "James Wiseman", "Cassius Winston", "Justise Winslow", "Dylan Windler", "D.J. Wilson", "Zion Williamson", "Robert Williams", "Patrick Williams", "Lou Williams", "Kenrich Williams", "Grant Williams", "Andrew Wiggins", "Greg Whittington", "Hassan Whiteside", "Derrick White", "Coby White", "Russell Westbrook", "Quinndary Weatherspoon", "Paul Watson", "Tremont Waters", "Yuta Watanabe", "P.J. Washington", "T.J. Warren", "Brad Wanamaker", "John Wall", "Lonnie Walker", "Kemba Walker", "Moe Wagner", "Dean Wade", "Nikola Vucevic", "Gabe Vincent", "Devin Vassell", "Fred VanVleet", "Jarred Vanderbilt", "Denzel Valentine", "Jonas Valanciunas", "Myles Turner", "Rayjon Tucker", "P.J. Tucker", "Gary Trent, Jr.", "Karl-Anthony Towns", "Juan Toscano-Anderson", "Obi Toppin", "Xavier Tillman, Sr.", "Killian Tillie", "Matisse Thybulle", "Sindarius Thornwell", "Tristan Thompson", "Klay Thompson", "Matt Thomas", "Brodric Thomas", "Daniel Theis", "Tyrell Terry", "Garrett Temple", "Jeff Teague", "Jayson Tatum", "Jae'sean Tate", "Edmond Sumner", "Max Strus", "Isaiah Stewart II", "Lamar Stevens", "Cassius Stanley", "Tony Snell", "Jalen Smith", "Ish Smith", "Dennis Smith", "Marcus Smart", "Alen Smailagic", "Deividas Sirvydis", "Anfernee Simons", "Ben Simmons", "Chris Silva", "Pascal Siakam", "Iman Shumpert", "Landry Shamet", "Collin Sexton", "Jayden Scrubb", "Mike Scott", "Dennis Schroder", "Tomas Satoransky", "Dario Saric", "JaKarr Sampson", "Luka Samanic", "Domantas Sabonis", "D'Angelo Russell", "Ricky Rubio", "Terry Rozier", "Terrence Ross", "Derrick Rose", "Rajon Rondo", "Isaiah Roby", "Mitchell Robinson", "Jerome Robinson", "Duncan Robinson", "Andre Roberson", "Austin Rivers", "Grant Riller", "Josh Richardson", "Nick Richards", "Naz Reid", "Paul Reed, Jr.", "J.J. Redick", "Cam Reddish", "Julius Randle", "Chasson Randle", "Jahmi'us Ramsey", "Immanuel Quickley", "Payton Pritchard", "Taurean Prince", "Norman Powell", "Dwight Powell", "Kristaps Porzingis", "Bobby Portis", "Otto Porter", "Michael Porter, Jr.", "Kevin Porter, Jr.", "Jontay Porter", "Jordan Poole", "Aleksej Pokusevski", "Vincent Poirier", "Jakob Poeltl", "Mason Plumlee", "Theo Pinson", 
            "Reggie Perry", "Norvel Pelle", "Elfrid Payton", "Cameron Payne", "Chris Paul", "Justin Patton", "Patrick Patterson", "Eric Paschall", "Jabari Parker", "Kelly Oubre, Jr.", "Daniel Oturu", "Cedi Osman", "Miye Oni", "Kelly Olynyk", "Victor Oladipo", "KZ Okpala", "Isaac Okoro", "Onyeka Okongwu", "Josh Okogie", "Chuma Okeke", "Jahlil Okafor", "Semi Ojeleye", "Royce O'Neale", "Jordan Nwora", "David Nwaba", "Jusuf Nurkic", "Kendrick Nunn", "Frank Ntilikina", "Jaylen Nowell", "Nerlens Noel", "Zeke Nnaji", "Georges Niang", "Raulzinho Neto", "Aaron Nesmith", "Larry Nance, Jr.", "Abdel Nader", "Svi Mykhailiuk", "Mike Muscala", "Jamal Murray", "Dejounte Murray", "Mychal Mulder", "Monte Morris", "Markieff Morris", "Marcus Morris", "Juwan Morgan", "Ja Morant", "E'Twaun Moore", "Malik Monk", "Adam Mokoka", "Donovan Mitchell", "Shake Milton",
            "Paul Millsap", "Patty Mills", "Darius Miller", "Khris Middleton", "Chimezie Metu", "Sam Merrill", "De'Anthony Melton", "Nicolo Melli", "Ben McLemore", "Jordan McLaughlin", "Alfonzo McKinnie", "Rodney McGruder", "JaVale McGee", "Sean McDermott", "Doug McDermott", "Jalen McDaniels", "Jaden McDaniels", "T.J. McConnell", "C.J. McCollum", "Patrick McCaw", "Skylar Mays", "Tyrese Maxey", "Wesley Matthews", "Garrison Mathews", "Kelan Martin", "K.J. Martin", "Cody Martin", "Caleb Martin", "Naji Marshall", "Lauri Markkanen", "Boban Marjanovic", "Nico Mannion", "Terance Mann", "Karim Mane", "Theo Maledon", "Will Magnay", "Trey Lyles", "Timothe Luwawu-Cabarrot", "Kyle Lowry", "Kevin Love", "Robin Lopez", "Brook Lopez", "Kevon Looney", "Nassir Little", "Damian Lillard", "Kira Lewis, Jr.", "Caris LeVert", "Meyers Leonard", "Kawhi Leonard", "Alex Len", "Saben Lee", "Damion Lee", "Jalen Lecque", "Jake Layman", "Zach LaVine", "Romeo Langford", "Jeremy Lamb", "Kyle Kuzma", "Rodions Kurucs", "Luke Kornet", "Furkan Korkmaz", "John Konchar", "Kevin Knox", "Nathan Knight", "Maxi Kleber", "Luke Kennard", "Enes Kanter", "Frank Kaminsky", "Mfiondu Kabengele", "Cory Joseph", "DeAndre Jordan", "Tyus Jones", "Tre Jones", "Mason Jones", "Derrick Jones", "Damian Jones", "Nikola Jokic", "Tyler Johnson", "Stanley Johnson", "Keldon Johnson", "James Johnson", "Cameron Johnson", "Isaiah Joe", "Ty Jerome", "DaQuan Jeffries", "LeBron James", "Justin James", "Reggie Jackson", "Justin Jackson", "Jaren Jackson, Jr.", "Josh Jackson", "Frank Jackson", "Wesley Iwundu", "Jonathan Isaac", "Kyrie Irving", "Brandon Ingram", "Joe Ingles", "Andre Iguodala", "Serge Ibaka", "Chandler Hutchison", "De'Andre Hunter", "Elijah Hughes", "Kevin Huerter", "Markus Howard", "Dwight Howard", "Danuel House", "Talen Horton-Tucker", "Al Horford", "Rodney Hood", "Richaun Holmes", "Justin Holiday", "Jrue Holiday", "Aaron Holiday", "Nate Hinton", "Solomon Hill", "George Hill", "Buddy Hield", "Tyler Herro", "Willy Hernangomez", "Juancho Hernangomez", "Gordon Hayward", "Killian Hayes", "Jaxson Hayes", "Udonis Haslem", "Isaiah Hartenstein", "Josh Hart", "Tobias Harris", "Joe Harris", "Jalen Harris", "Gary Harris", "Montrezl Harrell", "Jared Harper", "Maurice Harkless", "James Harden", "Tim Hardaway Jr.", "R.J. Hampton", "Josh Hall", "Donta Hall", "Tyrese Haliburton", "Rui Hachimura", "Kyle Guy", "Blake Griffin", "Josh Green", "Jeff Green", "Javonte Green", "JaMychal Green", "Draymond Green", "Danny Green", "Jerami Grant", "Devonte' Graham", "Eric Gordon", "Aaron Gordon", "Brandon Goodwin", "Rudy Gobert", "Anthony Gill", "Shai Gilgeous-Alexander", "Harry Giles", "Taj Gibson", "Paul George", "Rudy Gay", "Marc Gasol", "Darius Garland", "Langston Galloway", "Danilo Gallinari", "Daniel Gafford", "Wenyen Gabriel", "Markelle Fultz", "De'Aaron Fox", "Evan Fournier", "Trent Forrest", "Bryn Forbes", "Malachi Flynn", "Dorian Finney-Smith", "Bruno Fernando", "Terrance Ferguson", "Cristiano Felicio", "Derrick Favors", "Tacko Fall", "Dante Exum", "Drew Eubanks", "James Ennis", "Joel Embiid", "Wayne Ellington", "C.J. Elleby", "Carsen Edwards", "Anthony Edwards", "Kevin Durant", "Kris Dunn", "Jared Dudley", "Andre Drummond", "Goran Dragic", "P.J. Dozier", "Sekou Doumbouya", "Devon Dotson", "Damyean Dotson", "Luguentz Dort", "Luka Doncic", "Donte DiVincenzo", "Spencer Dinwiddie", "Gorgui Dieng", "Hamidou Diallo", "Mamadi Diakite", "DeMar DeRozan", "Matt Dellavedova", "Terence Davis", "Ed Davis", "Anthony Davis", "Nate Darling", "Stephen Curry", "Seth Curry", "Jarrett Culver", "Jae Crowder", "Torrey Craig", "Robert Covington", "Tyler Cook", "Pat Connaughton", "Mike Conley", "Zach Collins", "John Collins", "Amir Coffey", "Nicolas Claxton", "Jordan Clarkson", "Brandon Clarke", "Gary Clark", "Marquese Chriss", "Chris Chiozza", "Willie Cauley-Stein", "Alex Caruso", "Michael Carter-Williams", "Wendell Carter, Jr.", "Jevon Carter", "Vernon Carey, Jr.", "Clint Capela", "Vlatko Cancar", "Facundo Campazzo", "Kentavious Caldwell-Pope", "Devontae Cacok", "Jimmy Butler", "Alec Burks", "Trey Burke", "Reggie Bullock", "Thomas Bryant", "Jalen Brunson", "Sterling Brown", "Moses Brown", 
            "Troy Brown, Jr.", "Bruce Brown, Jr.", "Jaylen Brown", "Dillon Brooks", "Malcolm Brogdon", "Miles Bridges", "Mikal Bridges", "Ignas Brazdeikis", "Jarrell Brantley", "Tony Bradley", "Avery Bradley", "Brian Bowen II", "Chris Boucher", "Devin Booker", "Isaac Bonga", "Bol Bol", "Bojan Bogdanovic", "Bogdan Bogdanovic", "Keljin Blevins", "Eric Bledsoe", "Nemanja Bjelica", "Bismack Biyombo", "Goga Bitadze", "Khem Birch", "Tyler Bey", "Saddiq Bey", "Patrick Beverley", "Davis Bertans", "DeAndre' Bembry", "Malik Beasley", "Bradley Beal", "Darius Bazley", "Kent Bazemore", "Aron Baynes", "Nicolas Batum", "Keita Bates-Diop", "Will Barton", "R.J. Barrett", "Harrison Barnes", "Desmond Bane", "Mohamed Bamba", "Lonzo Ball", "LaMelo Ball", "Marvin Bagley III", "Dwayne Bacon", "Udoka Azubuike", "Deandre Ayton", "Deni Avdija", "D.J. Augustin", "Trevor Ariza", "Ryan Arcidiacono", "Ogugua Anunoby", "Cole Anthony", "Carmelo Anthony", "Thanasis Antetokounmpo", "Kostas Antetokounmpo", "Giannis Antetokounmpo", "Kyle Anderson", "Al-Farouq Aminu", "Jarrett Allen", "Grayson Allen", "Nickeil Alexander-Walker", "Ty-Shon Alexander", "LaMarcus Aldridge", "Bam Adebayo", "Steven Adams", "Jaylen Adams", "Precious Achiuwa"]

def playerIdsToJson():
    message = ''
    try:
        tempDict = {}
        playerBioInfo = {}
        playerNames = {}

        url = "https://api-nba-v1.p.rapidapi.com/players/league/standard"

        headers = {
            'x-rapidapi-key': "<< ACCESS TOKEN >>",
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        results = response.json()['api']['players']

        for i in range(len(results)):
            player = results[i]
            name = player['firstName'] + ' ' + player['lastName']
            if(name not in allPlayers): continue
            playerID = player['playerId']
            playerNames[name] = i
            name = name.lower()
            tempDict[name] = playerID
            team = ''
            try:
                team = team_id[int(player['teamId'])]
            except:
                team = ''
            school = player['collegeName']
            dob = player['dateOfBirth']
            height = player['heightInMeters']
            weight = player['weightInKilograms']

            if((team is None) or (team =='')):
                team = "n/a"
            if((school is None) or (school =='')):
                school = "n/a"
            if((dob is None) or (dob =='')):
                dob = "n/a"
            if((height is None) or (height =='')):
                height = "n/a"
            if((weight is None) or (weight =='')):
                weight = "n/a"

            tempBioInfo = {}
            tempBioInfo['team'] = team
            tempBioInfo['college'] = school
            tempBioInfo['dob'] = dob
            tempBioInfo['height'] = height
            tempBioInfo['weight'] = weight
            playerBioInfo[name] = tempBioInfo


        with open("./data/players.json", "w") as outfile:  
            json.dump(tempDict, outfile)
        
        with open("./data/playersBioInfo.json", "w") as outfile:  
            json.dump(playerBioInfo, outfile)

        with open("./data/playerNames.json", "w") as outfile:  
            json.dump(playerNames, outfile)

        message = 'Players updated'
    except Exception as e:
        message = str(e)
        print(str(e))
    return message


def validGameIDsToJson():
    message = ''
 
    validGameIDs = []
    gameDates = {}

    url = "https://api-nba-v1.p.rapidapi.com/games/seasonYear/2020"

    headers = {
        'x-rapidapi-key': "<< ACCESS TOKEN >>",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    result = response.json()['api']['games']
    for i in range(len(result)):
        if(i<55): continue
        game = result[i]
        validGameIDs.append(game['gameId'])
        fullDate = game['startTimeUTC']
        date = ''
        try:
            fullDate = fullDate.replace('T', ' ')
            fullDate = fullDate.replace('.000Z', '')
            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('America/New_York')
            utc = datetime.strptime(fullDate, '%Y-%m-%d %H:%M:%S')
            utc = utc.replace(tzinfo=from_zone)
            fullDate = str(utc.astimezone(to_zone))
            spaceIndex = fullDate.index(' ')
            date = fullDate[0:spaceIndex]
        except Exception as e:
            print(e)
            date = fullDate
        
        gameDates[game['gameId']] = date

    with open("./data/validGames.json", "w") as outfile:  
        json.dump(validGameIDs, outfile)

    with open("./data/gameDateInfo.json", "w") as outfile:  
        json.dump(gameDates, outfile)

    message = 'Updated games'

    return message

def getPlayerID(playerName):
    f = open('./data/players.json')
    playerDict = json.load(f)
    return playerDict[playerName]

