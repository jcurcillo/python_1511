"""
Lab3_jcurcillo_remove.py
Author: Jack Curcillo
Purpose: Remove 'binoculars'
Date: 9/11/2025
"""

import Lab3_jcurcillo_replace

items = Lab3_jcurcillo_replace.items

if 'binoculars' in items:
    items.remove('binoculars')

print('Removed:', items)