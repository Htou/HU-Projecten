from Mastermind.mastermind_globals import *
import random


def generatecode():
    genCode = random.choices(colors, k=4)
    print("Er is een geheime kleurcode gegenereerd:", genCode)
    for i in genCode:
        sCode.append(i)
