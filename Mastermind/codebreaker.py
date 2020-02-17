from Mastermind.mastermind_globals import *
from Mastermind.visualizer import *
from Mastermind.feedbackgiver import *


def guesses():
    for i in range(4):
        print("")
        print(colors)
        board[playingRow][i] = input("Stel een code samen voor rij: " + str(row) + ", met de bovenstaande kleuren: ")
        print("")
        visualizer()


