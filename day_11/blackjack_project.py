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
"""
use one value of 10 to avoid a sum of 21 in the first round
"""
# Jack = 10 # Queen = 10 # King = 10

Ace = 11
cards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10]
play_agin = True
get_anther_card = True
auto_lose = False


def random_card():  ## function tha pick a random card form cards list
    return random.choice(cards)


your_cards = [random_card(), random_card()]
computer_cards = [random_card(), random_card()]


def computer_playing_algorithm(computer_cards: list, cards_sum):
    """
    function responsible for the algo of computer picking mor cards in his turn.
    return a list : [list: all computer cards , int: the sum of those cards].
    """
    while cards_sum < 17:
        computer_cards.append(random_card())
        cards_sum = sum(computer_cards)
    return [computer_cards, cards_sum]


def check_winner(your_cards, computer_after_paly: list):
    """
    function to check the winner under the blackjack rules
    """
    res_message = "You went over!!! You lost"
    if sum(your_cards) > 21:
        res_message = "You went over!!! You lost"
    elif computer_after_paly[1] > 21:
        res_message = "congratulations you win"

    else:
        if 21 - sum(your_cards) < 21 - computer_after_paly[1]:
            res_message = "congratulations you win"
    print("\n********************************************************")
    print(res_message)
    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(
        f"computer final hand : {computer_after_paly[0]}, final score: {computer_after_paly[1]} "
    )
    print("\n********************************************************")


while play_agin:
    yes_No_playing = input("Do you wont to play Blackjack?: Type 'y' or 'n': ").lower()
    if yes_No_playing == "n":
        print("goodby!!!!")
        break

    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"computer first card: {computer_cards[0]}")

    while get_anther_card:
        anther_card = input("Type 'y' to get anther card; 'n' to pass: ").lower()
        if anther_card == "n":
            get_anther_card = False
            computer_after_paly = computer_playing_algorithm(
                computer_cards, sum(computer_cards)
            )
            check_winner(your_cards, computer_after_paly)
            break

        else:
            your_cards.append(random_card())
            if sum(your_cards) >= 21:
                play_agin = False
                computer_after_paly = computer_playing_algorithm(
                    computer_cards, sum(computer_cards)
                )
                check_winner(your_cards, computer_after_paly)
                break
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"computer first card: {computer_cards[0]}")
