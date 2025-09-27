"""
Lab4_jcurcillo-1.py
Author: Jack Curcillo
Purpose: Choose x amount of random cards (no repeats).
Date: 9/16/2025
"""
import random

keep_dealing = 'y'

while keep_dealing == 'y':
   
    cards = int(input('How many cards would you like? (1-52): '))

    while cards > 52 or cards < 1:
        cards = int(input('Please choose a number between 1 and 52: '))

    card_value = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_suit = ["♣️", "♥️", "♠️", "♦️" ] 

    possible_cards = []
    for value in card_value:
        for suit in card_suit:
            possible_cards.append(f'{value}{suit}')

    print('Your hand is:', end= ' ')

    for i in range(cards):
        card = random.choice(possible_cards)
        possible_cards.remove(card)
        print(card, end='  ')
    
    print()

    keep_dealing = input('Would like another set of cards? (y or n): ').lower()
    while keep_dealing != "y" and keep_dealing != "n":
        keep_dealing = input("Please enter y or n: ").lower()