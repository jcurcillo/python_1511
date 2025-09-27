"""
Lab3_jcurcillo_add.py
Author: Jack Curcillo
Purpose: Add 5 items to camping list
Date: 9/11/2025
"""

import Lab3_jcurcillo_list

items = Lab3_jcurcillo_list.items

to_add = ['grill', 'toothbrush', 'deoderant', 'cash', 'lighter']

items.extend(to_add)

print('New Items:', items)
