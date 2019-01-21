# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:53:03 2018

@author: leann
"""


######  Chapter 11 - The 'While Loop'  ########


###  in class exercise #####
x = 33
while x >= 1:
    print(x, ':', end='')
    x = x / 2
    print(x)
    


x = 100
while x >= 1:
    print(x, ':', end='')
    x = x / 2
    print(x)



###   making triangular number (in class)    ####

def triangular(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    return sum 

def triangular(n):
    triangularSum = 0
    triangularSum = int(triangularSum)
    while n > 0:
        triangularSum = triangularSum + n
        n = n - 1
    print(triangularSum)


####   Determining Students marks!   #####

#mark = 1
while mark > 0:
    mark = input('Enter your mark: ')
    mark = int(mark)
    print('Your mark is ', mark, end='') 
    if mark > 90:
        print('\n You\'re beyond first class, you\'ve gone off the scale. \nKeep it up!')   
    elif mark >= 70 and mark <= 90:
        print('\nWow there, first class marks for you!')
    elif mark >= 40:
        print('\nYou\'ve passed, wipe that sweat from your brow.')
    else: 
        print('\n Uh oh, sorry but you\'ve not done enough to pass.')
    

##  PRACTISING LOOPS ######

i = 26
while 1 > 10:
    print(i)
    i = i*0.8
    if i == 35.2:
        break
    

i = 1
while 1 <= 10:
    print(i)
    i = i + 1
    print('Done with this loop')
    
    
    
    ###practising writing 'True'  ####
while True:
    name = input('Enter your chosen name: ')
    if name == 'done':
        break
    print('Hello', name)
    

while True:
    name = input('Please enter your name: ')
    if name == 'not my name':
        break
    print('Hello there ', name)
    
    
###########---------   Guessing Game         --------################


from random import randint


def guess(guess_taken, ceiling):
    number = randint(1, ceiling)
    
    print('\nWelcome Game Players of the World!\n\nCan you guess my secret number?')
    yourName =input('Please enter your name to play....  ')
    print('\nA warm welcome {}' .format(yourName))
    print('\nI am thinking of a number.')
    
    while guess_taken > 0:
        
        
        print('\nTake a guess my friend,\n we will not bite.')
        guess = input('Enter your wisest number choice: ')
        guess = int(guess)
   
        if guess < number:
            print('Your guess is waay to low!')
            
        elif guess > number:
                print('Your guess has gone through the roof,\ncome back down!')
                
        elif guess == number:
            print('Your work here is done {}'.format(yourName), + 'CONGRATUALTIONS!')
            break
        
        guess_taken = guess_taken - 1
        print('You have {} '.format(guess_taken) + 'guesses left')
            
    print('This is the End -------GAME OVER ')
        
guess(6,100)


