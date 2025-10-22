"""
coin.py
Author: Jack Curcillo
Purpose: Define a coin object.
Date: 10/22/2025
"""

import random

class Coin:
    def __init__(self):
        """Initialize sideup to Heads or Tails, and amount to 20."""
        self.__sideup = 'Heads'
        self.__amount = 20

    def toss(self):
        """Randomly toss the coin and assign sideup to Heads or Tails."""
        toss_result = random.randint(0,1)
        if toss_result == 1:
            self.__sideup = 'Heads'
        if toss_result == 0:
            self.__sideup = 'Tails'
    
    def get_sideup(self):
        """Return the current side up."""
        return self.__sideup
    
    def set_amount(self, diff):
        """
        Change the amount of coins by +1 or -1.
        change: int, +1 or -1
        """
        self.__amount += diff

    def get_amount(self):
        """Return the current amount of coins."""
        return self.__amount
    

        
