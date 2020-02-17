from Mastermind.mastermind_globals import *

def generateFeedbackboard():
    x = len(board)
    for i in range(x):
        feedbackBoard.append([])
        for j in range(4):
            feedbackBoard[i].append("F")
    for k in feedbackBoard:
        return k


def feedback():
    for i in range(4):
        if board[playingRow][i] != mCode:
            print(board[playingRow][i])
