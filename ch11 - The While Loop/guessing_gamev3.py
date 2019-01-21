# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:12:01 2018

@author: leann
"""

#####  VERSION 2 - working on version    #######


from random import randint

def guess(guess_taken, inrange):
    number = randint(1, inrange)
    print('\nWelcome Game Players of the World!\n\nCan you guess my secret number?')
    
    yourName =input('Please enter your name to play....  ')
    print('\nA warm welcome {}' .format(yourName))
    print('\nI am thinking of a number.')
    
    guess = guess_taken
    result ='playing'
    
    while guess > 0:
        answer = int(input('Enter your wisest number choice: '))        
        if answer == number:
            result = 'win'
            print('Your work here is done {}'.format(yourName), + 'CONGRATUALTIONS!')
            break
     
        elif answer < number:
            print('Your guess is waay to low!')
            guess = guess -1
            
        elif guess > number:
                print('Your guess has gone through the roof,\ncome back down!')
                guess = guess -1

#        guess_taken = guess_taken - 1
        print('You have {} '.format(guess_taken) + 'guesses left')
   
    if result != 'win':         
        print('This is the End -------GAME OVER ')
        
guess(6,100)
