from Mastermind.mastermind_globals import *


def guesses():
    for i in range(4):
        print("")
        print(collors)
        board[playingRow][i] = input("Stel een code samen voor rij: " + str(row) + " met de bovenstaande kleuren ")
        print("")
        for j in board:
            print(j)


def nextRow():
    global row
    global playingRow
    row += 1
    playingRow = playingRow - 1
