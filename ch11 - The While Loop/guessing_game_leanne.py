# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:33:56 2018

@author: leann
"""

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