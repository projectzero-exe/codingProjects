
import random
from time import sleep



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

player1 = []
computer = []

def drawingCards():
    draw, draw1 = random.choice(list(deck_ofCards.items()))
    #print(draw, draw1)
    used_deck[draw] = draw1
    del deck_ofCards[draw]
    return draw, draw1

def computerDrawing():
    compK, compV = drawingCards()
    computer.append(compV)
    print(compK)
    return compK, compV


def playerDrawing():
    playerK, playerV = drawingCards()
    player1.append(playerV)
    print(playerK)
    return playerK, playerV



#print(f"Player1 cards are {card1} and {card2}")

card1, cardVP1 = playerDrawing()
card3, cardCP1 = computerDrawing()
card2, cardVP2 = playerDrawing()
card4, cardCP2 = computerDrawing()
print(f"House cards: {card4}")
print(f"Player1 cards are {card1} and {card2}")

while True:

    
    draw_next = input("Would you like to draw another card? Type ('yes') or ('no'): ").lower()
    if cardVP1 == 11 or cardVP2 == 11:
        x = input("Would you like to keep it as 11 or change it to 1? "
              "\ntype 'yes' to change the value or 'no' to keep the card as is: ").lower
        if x == 'yes' or x == 'y':
            player1.sort(reverse=True)
            player1[0] = 1
    if draw_next == "y" or draw_next == "yes":
        card5, cardVP3 = playerDrawing()
        print(f"Player1 cards are {card1}, {card2} and {card5}")
        res = sum(player1)
        resC = sum(computer)
        print(res)
        print(resC)
        # if cardVP3 == 11:

    # else:
    #     break

