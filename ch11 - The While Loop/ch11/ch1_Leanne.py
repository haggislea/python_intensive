# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:53:03 2018

@author: leann
"""


#i = 1
#while 1 <= 10:
#    print(i)
#    i = i + 1
#    print('Done with this loop')
    
    
#while True:
#    name = input('Enter your name: ')
#    if name == 'done':
#        break
#    print('Hello', name)


mark = 1
while mark > 0:
    mark = input('Enter your mark: ')
    mark = int(mark)
    print('Your mark is', mark, end='')
    if mark >= 100:
        print('Pretty amazing and slightly unbeleivable!')
    if mark >= 70:
        print(' - great! First class for you')
    elif mark >= 40:
        print('- that\'s a pass.')
    elif mark <= 39:
        print('- sadly this is a fail')
    else:
        if mark == 'finish':
            print('Your time here is done')