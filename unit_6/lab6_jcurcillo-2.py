"""
Lab6_jcurcillo-2.py
Author: Jack Curcillo
Purpose: Create a guessing game with numbers 1-100
Date: 10/05/2025
"""


import random

catalog = {
    'number': random.randint(1, 100),
    'guesses': 0
}

guess = 0

while guess != catalog['number']:
    guess = int(input('Enter your guess! (1-100): '))
    catalog['guesses'] += 1
    if guess == catalog['number']:
        print(f'You got it! ({catalog['guesses']} guesses)')
    elif catalog['guesses'] % 2 == 0 and guess < catalog['number']:
        print('Hmm, try a bigger number. ')
    elif catalog['guesses'] % 2 == 0 and guess > catalog['number']:
        print('Let\'s try a little smaller. ')
    else:
        print('Try again! ')
    