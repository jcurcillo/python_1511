"""
Lab5_jcurcillo-1.py
Author: Jack Curcillo
Purpose: Roll 2 die and output the corresponding statement.
Date: 9/24/2025
"""

import random

roll_again = 'y'

while roll_again == 'y':
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2

    print(f'Dice 1: {dice_1}')
    print(f'Dice 2: {dice_2}')
    print(f'Total: {dice_1 + dice_2}')

    if total == 2:
        print("Snake Eyes")
    elif total == 3:
        print("Ace Caught a Deuce")
    elif dice_1 == 2 and dice_2 == 2:
        print("Little Joe from Kokomo")
    elif total == 5:
        print("Little Phoebe")
    elif dice_1 == 3 and dice_2 == 3:
        print("Jimmy Hicks from the Sticks")
    elif (dice_1 == 6 and dice_2 == 1) or (dice_1 == 1 and dice_2 == 6):
        print("Six Ace")
    elif dice_1 == 4 and dice_2 == 4:
        print("Eighter from Decatur")
    elif total == 9:
        print("Nina from Pasadena")
    elif dice_1 == 5 and dice_2 == 5:
        print("Puppy Paws")
    elif (dice_1 == 6 and dice_2 == 5) or (dice_1 == 5 and dice_2 == 6):
        print("Six Five no Jive")
    elif total == 12:
        print("Boxcars")
    else:
        print("No nickname for this roll.")

    roll_again = input('Would like to roll again? (y or n): ').lower()
    while roll_again != "y" and roll_again != "n":
        roll_again = input("Please enter y or n: ").lower()