
from circle import *
from square import *

while True:
    #get choice
    choice = 0
    while choice < 1 or choice > 5:
        choice = int(input("Menu\n1) Circle Area\n2) Circle Circumference\n3) Rectangle Area\n" \
        "4) Rectangle Perimeter\n5) Quit\nEnter your choice: "))
        if choice == 5:
            print("Exiting")
            break
        if choice < 1 or choice > 4:
            print("Please choose a number between 1 and 4.") 

    if choice == 5:
        break
    #circle calculations
    if choice == 1 or choice == 2:
        radius = float(input("What is the radius of the circle? - "))
        if choice == 1:
            area = circle_area(radius)
            print(f'The area of the circle is {area}')
        elif choice == 2:
            circumference = circle_circumference(radius)
            print(f'The circumference of the circle is {circumference}')

    #rectangle calculations
    if choice == 3 or choice == 4:
        length = float(input("What is the length of the rectangle? - "))
        width = float(input("What is the width of the rectangle? - "))

        if choice == 3:
            area = rectangle_area(length, width)
            print(f'The area of the rectangle is {area}')
        elif choice == 4:
            perimeter = rectangle_perimeter(length, width)
            print(f'The perimeter of the rectangle is {perimeter}')