"""
Program: Lab1_curcillo-1.py
Author: Jack Curcillo
Purpose: Show recommended tips and totals for dinner given an input.
Date: 9/6/2025
"""

total = float(input('Enter meal price: '))
print(f'Meal total: ${total:.2f}')
tip_1 = total * .15
tip_2 = total * .2
print(f'Tip 15%: ${tip_1:.2f}')
print(f'Tip 20%: ${tip_2:.2f}')
print(f'Total with 15% tip: ${total + tip_1:.2f}')
print(f'Total with 20% tip: ${total + tip_2:.2f}')
input("Press Enter to exit5")
