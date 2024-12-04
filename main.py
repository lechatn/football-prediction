import requests
import json
from InitJson import updateData
from nextGame import nextGamePrediction, selectTeam, askUpdate

#with open("data.json", "r") as f:
    #data = json.load(f)
   # for match in data['matches']:
        #if match['score']['fullTime']["away"] != None: 
           # print(match['homeTeam']['name'], match['score']['fullTime']["home"], "-" ,match['score']['fullTime']["away"], match['awayTeam']['name'])
       # else:
           # nextGamePrediction(match['homeTeam']['name'],match['awayTeam']['name'])
           # break
askUpdate()
homeTeam = selectTeam()
awayTeam = selectTeam(homeTeam)
print("vosua allez etudié le match entre", homeTeam, "et", awayTeam)

