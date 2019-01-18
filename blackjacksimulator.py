import math
import random

#known problems
#problem with cheat/cheater
#improve player strategy

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if (card == 11):
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
    return (hand)

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11:
                total+= 1
            else:
                total+= 11
        else:
            total += card
    return total


def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand


def dealer(dealer_hand):
    dealer_hand = deal(deck)
    while (total(dealer_hand) < 17):
        hit(dealer_hand)
    return (dealer_hand)

def player(player_hand, cheat):
    player_hand = deal(deck)
    while (total(player_hand) < 17):
        hit(player_hand)
    while ((total(player_hand) < 19) and (cheat < 0)):
        hit(player_hand)
    return(player_hand)

def cheater(player_hand, dealer_hand, cheat):
    for card in (player_hand + dealer_hand):
        if (card == "J" or card == "Q" or card == "K" or card == 10 or card == 9 or card == 8):
            cheat = cheat - 1
        else:
            cheat = cheat + 1
    return (cheat)



def game(winnings, dealer_hand, player_hand, cheat):
    dlr = dealer(dealer_hand)
    plr = player(player_hand, cheat)
    if (total(plr) > 21):
        winnings = winnings - 1
    elif (total(dlr) > 21):
        winnings = winnings + 1
    elif (total(dlr) >= total(plr)):
        winnings = winnings - 1
    else:
        winnings = winnings + 1

    cheat = cheater(plr, dlr, cheat)
    print ("player hand: ", plr)
    print ("dealer hand: ", dlr)
    print ("current card count: ", cheat)
    return (winnings)




deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*16
winnings = 0
player_hand = []
dealer_hand = []
cheat = 0

for i in range(1):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*16
    winnings = 0
    player_hand = []
    dealer_hand = []
    cheat = 0
    while (len(deck) > 10):
        winnings = game(winnings, dealer_hand, player_hand, cheat)
        print ("Winnings: " , winnings)
