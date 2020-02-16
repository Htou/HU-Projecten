from Mastermind.mastermind_globals import *
import random


def generateCode():
    global mCode
    mCode = random.choices(collors, k=4)
    print("Er is een geheime kleurcode gegenereerd:", mCode)
