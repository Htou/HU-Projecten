from Mastermind.mastermind_globals import *


def feedback():
    for i in range(4):
        if board[playingRow][i] != mCode:
            print(board[playingRow][i])
