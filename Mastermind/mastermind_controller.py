from Mastermind.mastermind_globals import *
from Mastermind.code_generator import *
from Mastermind.board_generator import *
from Mastermind.codebreaker import *
from Mastermind.feedbackgiver import *

generateCode()
generateBoard()

feedback()

# for i in board:
#     guesses()
#     feedback()
#     nextRow()