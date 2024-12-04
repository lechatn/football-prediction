import requests
import json

def checkseasonGoalTaked(team):
    with open("data.json", "r") as f:
        data = json.load(f)
        total = 0
        for match in data['matches']:
            if match['homeTeam']['name'] == team and match['status'] == "FINISHED":
                total += int(match['score']['fullTime']["away"])
            elif match['awayTeam']['name'] == team and match['status'] == "FINISHED":
                total += int(match['score']['fullTime']["home"])
        print(f"{team} a encaissé {total} buts cette saison")