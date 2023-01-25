import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    money = 1000
    while True:
        if money <= 0:
            print("Prohral jsi vsechno, jeste ze nehrajes o prave penize")
            print("Dekujeme za hru")
            sys.exit()

print('Penize:', money)
bet = getBet (money)
deck = getDeck()
dealerHand = [deck.pop(), deck.pop() ]
playerHand = [deck.pop(), deck.pop() ]
hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

barvy = ["S", "K", "P", "L"]

kredit = 300

balicek = []

karty_hrace = []

karty_dealera = []

balicek = [{"barva": barva, "hodnota": hodnota} for barva in barvy for hodnota in hodnoty]

random.shuffle(balicek)
