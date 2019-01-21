# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:52:32 2018

@author: leann
"""

print('You enter a dark creepy room with only two doors.\nDo you go through door#1 or door#2?')
      
door = input('')
if door == "1":
    print('There\'s a giant grizzly salivating bear eating a cheese cake\nWhat do you do?')
    print('1.Take the cake?')
    print('2. Scream at the bear?')
    
    bear = input('')
    
    if bear =="1":
        print('Oh damn, the bear has eaten your fingers')
    elif bear =='2':
        print('ewwww, the bear has eatern your legs,\nboth of them too!')
    else:
        print('Well, doing nothing is probably your best bet, the bear has run away!')
    
elif door == "2":
    print('You stare into the endless abyss at ZingZongs retina')
    print('1, Blueberries.')
    print('2. Yellow highViz jacket clothing.')
    print('3. Unerstanding the revolers yelling melodies.')

    insanity = input('')
    if insanity == '1' or insanity =='2':
        print('Your body survives for another day.\n Good job!')
    else:
        print('The insanty rots your eyes into a pool of muck. Good job!')
else:
    print('You stmble simlessly around and fall over bashing your\nhead and pass out, later eaten by zombies. The End')