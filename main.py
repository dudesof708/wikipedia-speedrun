#!/bin/python3

# I'll make this act more like a program later, quick programming

import os
import wikipedia

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def stats(cRound, playerList, playerScores, playerTimes):
    clear()
    print("nothing to do")

def gameRound(cRound, playerList, playerScores, playerTimes):
    clear()
    print("Current round:", cRound)
    begin, end = generateEndpoints()
    print("BEGIN AT:", begin, "\n  END AT:", end, '\n')
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

def menu():
    clear()
    print("Main Menu\n---------\n1 > Start Game\n2 > Generate Random Endpoints\n3 > Pathfind\n4 > Quit")
    incom = input()
    if incom.isnumeric():
        intcom = int(incom)
        if intcom == 1:
            game()
        elif intcom == 2:
            begin, end = generateEndpoints()
            print("You are going from", begin, "to", end)
        elif intcom == 3:
            pathfind()
        elif intcom == 4:
            exit(0)
    input("Press enter to continue.")
    menu()

def main():
    menu()

main()