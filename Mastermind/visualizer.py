from Mastermind.mastermind_globals import *


def visualizer():
    for i, j in zip(board, feedbackBoard):
        print('{}   {}'.format(i, j))
