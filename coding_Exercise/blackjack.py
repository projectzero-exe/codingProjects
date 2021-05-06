import random
from time import sleep
import numpy as np

# print(logo)
used_deck = {}
deck_ofCards = {
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
    "AceH": 11, "2H": 2, "3H": 3, "4H": 4,
    "5H": 5, "6H": 6, "7H": 7, "8H": 8,
    "9H": 9, "JH": 10, "QH": 10, "KH": 10,
    "AceS": 11, "2S": 2, "3S": 3, "4S": 4,
    "5S": 5, "6S": 6, "7S": 7, "8S": 8,
    "9S": 9, "JS": 10, "QS": 10, "KS": 10,
    "AceC": 11, "2C": 2, "3C": 3, "4C": 4,
    "5C": 5, "6C": 6, "7C": 7, "8C": 8,
    "9C": 9, "JC": 10, "QC": 10, "KC": 10,
    "AceD": 11, "2D": 2, "3D": 3, "4D": 4,
    "5D": 5, "6D": 6, "7D": 7, "8D": 8,
    "9D": 9, "JD": 10, "QD": 10, "KD": 10,
}


def drawingCards():
    draw, draw1 = random.choice(list(deck_ofCards.items()))
    print(draw, draw1)
    used_deck[draw] = draw1
    del deck_ofCards[draw]
    return draw, draw1

player1 = []
computer = []

compK, compV = drawingCards()

playerK, playerV = drawingCards()

compK1, compV1 = drawingCards()

playerK1, playerV1 = drawingCards()

player1.append(playerV)
computer.append(compV)
player1.append(playerV1)
computer.append(compV1)




res = sum(player1)
resC = sum(computer)
print(res)
print(resC)

# while True:
#     k, v = drawingCards()
#     print(f"K: {k}")
#     print(f"V: {v}")
#     if deck_ofCards == {}:
