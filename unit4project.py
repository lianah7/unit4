# by Liana Hill
# last updated October 15, 2019
# this program plays a game of blackjack with a dealer and user

import random


def get_card():
    """
    This function returns a random number between one and ten
    :return:
    """
    return random.randint(1, 10)


def starting_cards(card1, card2, total):
    print("You picked", card1, "and", card2)
    print("Your total is", total)


def main():
    get_card()
    card1 = get_card()
    card2 = get_card()
    total = card1 + card2
    starting_cards(card1, card2, total)
    additional_cards = input("Do you want another card? Enter 'y' for yes and 'n' for no.")
    card3 = get_card()
    user_total = card1 + card2 + card3
    if additional_cards =='y':
        card3 = get_card()
        user_total = card1 + card2 + card3
        print("Your new total is", user_total)
    else:
        print("Your total is still", total)
    if total > 21:
        print("You lost!")
    else:
        card4 = get_card()
        card5 = get_card()
        dealer_total = card4 + card5
        print("The dealer's cards are", card4, "and", card5)
        print("The dealer's total is", dealer_total)
        if dealer_total < user_total:
            print("You won!")
        elif dealer_total == user_total:
            print("You tied. The dealer wins!")
        else:
            print("You lost!")


main()
