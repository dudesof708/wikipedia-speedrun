#!/bin/python3

# I'll make this act more like a program later, quick programming

import os
import wikipedia

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    players = ""
    playerList = []
    clear()
    print("Game Menu\n---------")
    while not players.isnumeric():
        players = input("Number of players > ")
    players = int(players)
    for player in range(players):
        playerList[player] = input("Player " + player + "'s Name? ")
    playerScores = [0] * players
    clear()

def generateEndpoints():
    return [wikipedia.random(), wikipedia.random()]

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
            g = generateEndpoints()
            print("You are going from", g[0], "to", g[1])
        elif intcom == 3:
            pathfind()
        elif intcom == 4:
            exit(0)
    input("Press enter to continue.")
    menu()

def main():
    menu()

main()