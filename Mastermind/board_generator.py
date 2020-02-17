from Mastermind.mastermind_globals import *


def generateboard():
    x = int(input("Met hoeveel rijen wil je spelen? "))
    for i in range(x):
        board.append([])
        for j in range(4):
            board[i].append("X")
    for k in board:
        return k


def generatefeedbackboard():
    x = len(board)
    for i in range(x):
        feedbackBoard.append([])
    for j in feedbackBoard:
        return j
