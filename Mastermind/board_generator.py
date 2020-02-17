from Mastermind.mastermind_globals import *


def generateBoard():
    global board
    x = int(input("Met hoeveel rijen wil je spelen? "))
    for i in range(x):
        board.append([])
        for j in range(4):
            board[i].append("X")
    for k in board:
        print(k)
