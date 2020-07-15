#!/bin/python3

import os
import wikipedia

def generateEndpoints():
    ep = [wikipedia.random(), wikipedia.random()]
    print("You are going from", ep[0], "to", ep[1])

def pathfind():
    print("Feature coming soon.")

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""Main Menu
    ---------
    1 > Generate Random Endpoints
    2 > Pathfind
    3 > Quit
    """)
    incom = input()
    if incom.isnumeric():
        intcom = int(incom)
        if intcom == 1:
            generateEndpoints()
        elif intcom == 2:
            pathfind()
        elif intcom == 3:
            exit(0)
    input("Press enter to continue.")
    menu()

def main():
    menu()

main()