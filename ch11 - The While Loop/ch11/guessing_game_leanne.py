# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:33:56 2018

@author: leann
"""



###########   The Guessing Game      ###########
correct_guess = 97
print('\nWelcome! Can you guess my secret numer?')
guess = int(input('Enter a number: '))

guess_count = 0
guess_limit = 4
out_of_guesses = False

while correct_guess != guess:
    print
    if guess < correct_guess:
        print('Guess is waaaaay to low')
        guess = int(input('Have another go: '))
    elif guess > correct_guess:
        print('Too high, too high')
        guess = int(input('Have another go: '))
    elif guess != correct_guess:
         print('You have guessed supreme being!')      
    else:
        out_of_guesses = True
        print('GAME OVER.')

        
        
##
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
#

