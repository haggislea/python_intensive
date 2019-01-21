# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:18:31 2018

@author: leann
"""

#from random import randint
#def guess(attempts,range):
#    number = randint(1, range)
print('Welcome! Can you guess my secret numer?')
    
correct_guess = 97
guess = int(input('Enter a number: '))

guess_count = 0
guess_limit = 4
out_of_guesses = False

while correct_guess != guess:
    print
    if correct_guess == correct_guess:
        print('You have guessed supreme being!')   ##doesnt print out
    elif guess < correct_guess:
        print('Guess is waaaaay to low')
        guess = int(input('Have another go: '))
    elif guess > correct_guess:
        print('Too high, too high')
        guess = int(input('Have another go: '))
    else:
        out_of_guesses = True
        print('GAME OVER.')    


###### need to add this in
    
#while guess != correct_guess and not (out_of_guesses):
#
#        
#        
#    elif guess_count < guess_limit:
#        guess = input('Enter your guess: ')
#        guess 
#        print('Nope, try again')
#        guess_count += 1
#        
#    else:
#        out_of_guesses = True
#        print('LOSER! You bring shame on yourself.')