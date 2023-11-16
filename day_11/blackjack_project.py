"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

import logo
import random

# print(logo.logo)
Jack = 10
Queen = 10
King = 10
Ace = 11
cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
play_agin = True
get_anther_card = True


def random_num():
    return random.randint(0, len(cards) - 1)


while play_agin:
    yes_No_playing = input("Do you wont to play Blackjack?: Type 'y' or 'n': ").lower()
    if yes_No_playing == "n":
        print("goodby!!!!")
        break

    your_cards = [cards[random_num()], cards[random_num()]]
    computer_cards = [cards[random_num()], cards[random_num()]]

    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"computer first card: {your_cards[0]}")

    while get_anther_card:
        anther_card = input("Type 'y' to get anther card; 'n' to pass: ").lower()
        if anther_card == "n":
            get_anther_card = False
            print("you have ------ com have ------")
        else:
            your_cards.append(cards[random_num()])
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"computer first card: {your_cards[0]}")
