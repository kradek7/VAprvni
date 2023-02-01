import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main() :
    print()


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
        print('Sazka', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Sazka je navysena na {}.'.format(bet))
                print('Sazka:', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('Udelano {} z {}.'.format(rank, suit))
                playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                continue
            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Tah dealera...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                    input('Enter pro pokracovani...')
                    print('\n\n')

        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('Dealer to prepalil!, vyhravate {} $.'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Prohral jsi')
            money -= bet
        elif playerValue > dealerValue:
            print('Vyhral jsi {} $.'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('Remiza, vase sazka se vam pricte zpatky na konto')

        input('Enter pro pokracovani')
        print('\n\n')


def getBet(maxBet):
    while True:
        print('Kolik chcete vsadit? (1- {} nebo STORNO)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'STORNO':
            print('Dekujeme za hru, tesime se priste')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showdealerHand):
    print()
    if showdealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    print('Hrac:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H) vzit', '(S) zastavit']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D) zdvojnasobit')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()

        if move in ('H', 'S'):
            return move

        if move == 'D' and '(D) zdvojnasobit' in moves:
            return move


if __name__ == '__main__':
    main()




