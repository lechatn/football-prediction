from InitJson import returnclubs
from InitJson import updateData

def nextGamePrediction(myTeam, Team):
    #checkseasonGoalTaked(homeTeam)
    #checkseasonGoalTaked(awayTeam)
    #checkseasonGoalScored(homeTeam)
    #checkseasonGoalScored(awayTeam)
    return 

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
   
