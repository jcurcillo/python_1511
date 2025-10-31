"""
main.py
Author: Jack Curcillo
Purpose: Create a coin game using Coin class.
Date: 10/22/2025
"""

from coin import Coin

def main():
    #runs the game
    print('Welcome!')
    print('Each player starts with 20 coins.')
    play = input("Do you want to play? (Y/N): ").strip().lower()
    
    
   

    #creates quit game loop
    while play != 'n':
        # Create two players
        player_1 = Coin()
        player_2 = Coin()

        #define in-game loop
        again = 'y'
        print(f'Player 1: {player_1.get_amount()}')
        print(f'Player 2: {player_2.get_amount()}')
        while again != 'n':
            print('Flipping...')
            print()

            #toss
            player_1.toss()
            player_2.toss()
            print(f"Player 1 tosses: {player_1.get_sideup()}")
            print(f"Player 2 tosses: {player_2.get_sideup()}")
        
            #score
            if player_1.get_sideup() == player_2.get_sideup():
                print('Coins match!')
                diff1 = 1
                diff2 = -1
            else:
                print('Coins are different!')
                diff1 = -1
                diff2 = 1
            
            player_1.set_amount(diff1)
            player_2.set_amount(diff2)

            print(f'Player 1: {player_1.get_amount()}')
            print(f'Player 2: {player_2.get_amount()}')

            #check for winner
            if player_2.get_amount() == 0 or player_1.get_amount() == 0:
                break

            #reflip
            again = input("Do you want to flip again? (Y/N): ").strip().lower()
            
            
        #score the game
        if player_2.get_amount() == player_1.get_amount():
            print('It\'s a tie!')
        elif player_2.get_amount() < player_1.get_amount():
            print('Wow! Player 1 wins!')
            print('Good luck next time Player 2.')
        else:
            print('Congratulations Player 2!')
            print('Nice try Player 1')
        
        #play again
        play = input("Do you want to play again? (Y/N): ").strip().lower()
        
    print('Thanks for playing!')

    


if __name__ == '__main__':
    main()
