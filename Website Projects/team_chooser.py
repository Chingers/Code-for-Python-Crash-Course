#Team Choosers

#Imports random library
from random import choice


players = []
teamA = []
teamB = []
exitThis = 0
command = 0

#Functions
def choosePlayers(action):
    #Input Players
    done = 0
    while done == 0:

        if action == 'add':
            player = input("player(" + str(len(players) + 1) + ")(Type 'done' when done): ")
        elif action == 'remove':
            player = input("Player to remove(Type 'done' when done):")
            
        if player.lower() == 'done':
            done = 1            
        elif player == "":
            print("Please type in a name.")            
        else:
            if action == 'add':
                players.append(player)                
            elif action == 'remove':
                players.remove(player)

def randomizeTeams():
    teamA = []
    teamB = []
    #Creates teams in loop
    while len(players) > 0:

        playerA = choice(players)
        teamA.append(playerA)
        players.remove(playerA)

        playerB = choice(players)
        teamB.append(playerB)
        players.remove(playerB)

    #Shows teams
    print("Team A: " + str(teamA))
    print("Team B: " + str(teamB))

    for player in teamA:
        players.append(player)

    for player in teamB:
        players.append(player)

    teamA = []
    teamB = []

def removePlayers():
    done = 0
    while done == 0:

        player = input("Player to remove (Type 'done' when done): ")

        if player.lower() == 'done':
            done = 1            
        elif player == "":
            print("Please type in a name.")            
        else:
            players.remove(player)
        
while choice != 3:
    
    #initial Prompt
    command = input("(1) add, (2) randomize teams, (3) exit, (4) remove, (5) Show players: ")

    if command == "1":
        choosePlayers('add')
    elif command == "2":
        randomizeTeams()
    elif command == "3":
        exit()
    elif command == "4":
        choosePlayers('remove')
    elif command == "5":
        print(players)


    
    

    


    
