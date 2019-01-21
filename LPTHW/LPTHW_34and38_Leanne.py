# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:13:13 2018

@author: leann
"""

ten_things ="sausage, bacon, peas, icecream, loorolls, milk"

print('Hang on a minute there are not 10 items here!')

stuff = ten_things.split(' ')
more_stuff = ["sand", "sunshine", "bucket", "spade", "towel"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print('Adding: ')
    stuff.append('next_one')
    print('There are more items now '.len(stuff))
    
print('There we go:', stuff)

print('Let\'s do some things with our stuff now!')
print(stuff[1])
print(stuff[-2])
print(stuff.pop())
print (' ' .join(stuff))
print('#'.join(stuff[3:5]))