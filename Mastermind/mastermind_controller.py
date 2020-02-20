from Mastermind.code_generator import *
from Mastermind.board_generator import *
from Mastermind.codebreaker import *
from Mastermind.feedbackgiver import *
from Mastermind.visualizer import *


def upkeephuman():
    generatecode()
    generateboard()
    generatefeedbackboard()
    visualizer()
    for i in board:
        guesses()
        nextrow()
    feedback()
    print(feedbackBoard)


upkeephuman()
