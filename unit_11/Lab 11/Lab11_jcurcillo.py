
"""
Lab11_jcurcillo.py
Author: Jack Curcillo
Purpose: Create a program to count the frequency of words within a file. 
Date: 11/6/2025
"""
#func for getting simplified degrees
def simplify_rotation(degrees):
    return degrees % 360

def negative_simplify_rotation(degrees):
    return 360- degrees % 360

def type_verification(x):
    return float(x)

def main(): 
    try:
        rotation = input('Enter degrees of rotation: ')
        rotation = type_verification(rotation)
    except ValueError:
        print('Please enter a number value.')
    else:
        if rotation < 0:
            print(f'Rotation is {negative_simplify_rotation(rotation)} degrees ')
        else:
            print(f'Rotation is {simplify_rotation(rotation)} degrees ')



if __name__ == '__main__':
    main()