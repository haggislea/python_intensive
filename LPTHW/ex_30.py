# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:40:38 2018

@author: leann
"""

people = 30
cars = 40
buses = 15

if cars > people:
    print('We should take the cars.')
elif cars < people:
    print('We can\' take the cars')    
else:
    print('We can\'t decide!')
    
if buses > cars:
    print('That\'s too many buses')
elif buses < cars:
    print('Maybe we should take the bus?')
else:
    print('We still can\'t decide, there\'s too many options!')
    
if people > buses:
    print('Alright, let\'s take the bus then')
else:
    print('Fine. Let\'s walk then.')