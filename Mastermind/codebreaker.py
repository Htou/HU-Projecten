from Mastermind.mastermind_globals import *


def guesses():
    for i in range(4):
        print(collors)
        board[0][i] = input("Stel een code samen voor rij: " + str(row) + " met de bovenstaande kleuren ")
        print("")
        for j in board:
            print(j)
    print("")
