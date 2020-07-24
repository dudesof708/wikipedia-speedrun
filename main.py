"""
wikipedia-speedrun

A Wikipedia speedrunner for noobs. Uses various methods for people to
play Wikipedia speedrunning with each other.

(C) 2020 Gideon Tong and Dudes of 708
"""

import os
import wikipedia
from lib.Menu import Menu

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def stats(cRound, playerList, playerScores, playerTimes):
    clear()
    print("nothing to do")

def gameRound(cRound, playerList, playerScores, playerTimes):
    clear()
    print("Current round:", cRound)
    begin, end = generateEndpoints()
    print("BEGIN AT:", begin, "\n  END AT:", end, '\nENTER PLAYER ORDER >')
    return playerScores, playerTimes

def game():
    players = ""
    playerList = []
    cRound = 0
    clear()
    print("Game Menu\n---------")
    while not players.isnumeric():
        players = input("Number of players > ")
    players = int(players)
    for player in range(players):
        playerList.append(input("Player " + str(player + 1) + "'s Name? "))
    playerScores = [0] * players
    playerTimes = [0] * players
    e = ""
    while e != "e":
        cRound += 1
        playerScores, playerTimes = gameRound(cRound, playerList, playerScores, playerTimes)
        e = input("Press enter to continue or e to end the game > ")
    stats(cRound, playerList, playerScores, playerTimes)

def generateEndpoints():
    return wikipedia.random(), wikipedia.random()

def pathfind():
    print("Feature coming soon.")

def menu(intcom):
    if intcom == 1:
        game()
    elif intcom == 2:
        begin, end = generateEndpoints()
        clear()
        print("START LOCATION:", begin, "\n  END LOCATION:", end)
    elif intcom == 3:
        pathfind()
    elif intcom == 4:
        exit(0)
    input("\nPress enter to continue.")
    menu()

def main():
    myMenu = Menu(['Start Game', 'Generate Random Endpoints', 'Pathfind', 'Quit'])
    selection = myMenu.createMenu(waitValidated=True)
    menu(int(selection))

main()