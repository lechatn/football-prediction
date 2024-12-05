from InitJson import returnclubs
from InitJson import updateData
import json

def nextGamePrediction(Hometeam, Awayteam):
    averageGoalHomeTeam= averagegoal(Hometeam)
    print("averageGoalHomeTeam = ",averageGoalHomeTeam)
    averageGoalAwayTeam= averagegoal(Awayteam)
    print("averageGoalAwayTeam = ",averageGoalAwayTeam)
    averageGoalAtHome= averagegoalAtHome(Hometeam)
    print("averageGoalAtHome = ",averageGoalAtHome)
    averageGoalAway= averagegoalAway(Awayteam)
    #homeTeamStandings = standings(Hometeam)
    #awayTeamStandings = standings(Awayteam)

    return 


def averagegoal(team):
    print("team = ",team)
    with open(f"./ressources/standings.json", "r") as f:
        data = json.load(f)
    goals = 0
    played_games = 0
    for clubs in data["standings"][0]["table"]:
        if clubs["team"]["name"] == team:
            goals = clubs["goalsFor"]
            played_games = clubs["playedGames"]
            break
    return goals/played_games


def averagegoalAtHome(team):
    print("team = ",team)
    with open(f"./ressources/{team}.json", "r") as f:
        data = json.load(f)
    goals = 0
    played_games = 0
    for match in data["matches"]:
        if match["homeTeam"]["name"] == team and match["score"]["fullTime"]["home"] != None and match["competition"]["name"] == "Ligue 1":
            goals += match["score"]["fullTime"]["home"]
            played_games += 1
    return goals/played_games

def averagegoalAway(team):
    print("team = ",team)
    with open(f"./ressources/{team}.json", "r") as f:
        data = json.load(f)
    goals = 0
    played_games = 0
    for match in data["matches"]:
        if match["awayTeam"]["name"] == team and match["score"]["fullTime"]["away"] != None and match["competition"]["name"] == "Ligue 1":
            goals += match["score"]["fullTime"]["away"]
            played_games += 1
    return goals/played_games












def askUpdate():
    print("Do you want to update the data? (y/n)")
    update = input()
    if update == "y":
        updateData()
    elif update == "n":
        print("The data is up to date")
    else:
        print("Please enter a valid answer")
        askUpdate()

def selectTeam(homeTeam=None):
    print("Select the team you want to know the next game score:")
    clubs = returnclubs()
    if homeTeam != None:
        del clubs[homeTeam]
    number = 1
    for club in clubs.keys():
        print("["+str(number)+"]", club)
        number += 1
    team = input("Enter the number of the team: ")
    if not team.isdigit():
        print("Please enter a valid number")
        selectTeam()
    elif int(team) > len(clubs) or int(team) < 1:
        print("Please enter a valid number")
        selectTeam()
    team = list(clubs.keys())[int(team)-1]
    return team
   
