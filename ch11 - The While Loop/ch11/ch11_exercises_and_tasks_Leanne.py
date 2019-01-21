# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:53:03 2018

@author: leann
"""

### in class exercise
#x = 33
#while x >= 1:
#    print(x, ':', end='')
#    x = x / 2
#    print(x)
#    

#
#x = 100
#while x >= 1:
#    print(x, ':', end='')
#    x = x / 2
#    print(x)



###making triangular number (in class)

#def triangular(n):
#    sum = 0
#    while n > 0:
#        sum = sum + n
#        n = n - 1
#    return sum 

#def triangular(n):
#    triangularSum = 0
#    triangularSum = int(triangularSum)
#    while n > 0:
#        triangularSum = triangularSum + n
#        n = n - 1
#    print(triangularSum)


#### Determining Students marks!

#mark = 1
#while mark > 0:
#    mark = input('Enter your mark: ')
#    mark = int(mark)
#    print('Your mark is ', mark, end='') 
#    if mark > 90:
#        print('\n You\'re beyond first class, you\'ve gone off the scale. \nKeep it up!')   
#    elif mark >= 70 and mark <= 90:
#        print('\nWow there, first class marks for you!')
#    elif mark >= 40:
#        print('\nYou\'ve passed, wipe that sweat from your brow.')
#    else: 
#        print('\n Uh oh, sorry but you\'ve not done enough to pass.')
#    

##  PRACTISING LOOPS

#i = 26
#while 1 > 10:
#    print(i)
#    i = i*0.8
#    if i == 35.2:
#        break
#    

#i = 1
#while 1 <= 10:
#    print(i)
#    i = i + 1
#    print('Done with this loop')
#    
    
    
    ###practising writing 'True'
#while True:
#    name = input('Enter your chosen name: ')
#    if name == 'done':
#        break
#    print('Hello', name)
    

#while True:
#    name = input('Please enter your name: ')
#    if name == 'not my name':
#        break
#    print('Hello there ', name)
#    


####   exercise 6 chapter 11
    

####     my guessing game ######
#
#
secret_word = 'btfurther'

guess = ' '

guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input ('Enter guess:  ')
        guess_count += 1
          
    else: 
        out_of_guesses = True
        
        if out_of_guesses:
            print('Better luck next time.\nYou are out of guesses')
            
        if guess == secret_word: #### doesn't rpint this out
            print('Amazinglywonderful. How did you guess it?!!')        
            
            
            
            