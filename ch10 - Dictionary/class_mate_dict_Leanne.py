# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:39:46 2018

@author: leann
"""

#####  Classmate telephone dictionary
#to do:
#sort dictionary by name - alphabet
#sort by town and city - alphabet
#sort by dictionary by lucky no

#1. how many years differ from the queens age(QueenAge variable)
 
phoneBook = {}
users = 0

#def addAclassmate(phoneBook):
 
        
phonebook = {}
users = 0
while users < 4:
       print("-" * 50 )
       print('Welcome and Thank you classmate\n for taking part in our survey ')
       classmate1 = input("What's your name? ")
       print('\nA warm welcome {}' .format(classmate1))
       tel_num = input("What is the last 3 digits of your phone number? ")
       lady_luckNum = input("What is your luckiest of ever number? \n You know you have one..... ")
       users_age = int(input("What be your age? "))
       print('Don\'t worry we\'re not using these numbers for our lottery tickets!')
       place_living = input("Whereabouts are you living these days,\njust the name of the place will do.  ")
       postcode = input('\nLast but not least......\n What is the first letter of your postcode?')
       
       #  queens_age = 92
       if users_age == 'users_age' :
           print('You and the Queen are the same age!\n How about that!!')

       users = users + 1
       if users == 4:
           print("Thank you for entering these details.")


       phonebook[classmate1] = (classmate1, tel_num, lady_luckNum, users_age, place_living, postcode)
       print (phonebook)
print (phonebook)
#return phonebook

phonebook = input_phone_book()
print('thank you kindly for taking part')
    
    

####### prints as such ---- version one:

What's your name? 
eddie

What is the last 3 digits of your phone number? 
112

What is your lucky number? If you don't know, take a guess. 
234

How old are you? 
23

What Town/City do you live in? 
tiverton
{'eddie': ('112', '234', 23, 'tiverton')}



#
###### prints as such ---- #######version two:

Welcome and Thank you classmate
 for taking part in our survey 

What's your name? Vesper the Tester

A warm welcome Vesper the Tester

What is the last 3 digits of your phone number? 645

What is your luckiest of ever number? 
 You know you have one..... 2

What be your age? 15
Don't worry we're not using these numbers for our lottery tickets!

Whereabouts are you living these days,
just the name of the place will do.  Scotland


Last but not least......
 What is the first letter of your postcode? E
{'Vesper the Tester': ('Vesper the Tester', '645', '2', 15, 'Scotland', ' E')}
--------------------------------------------------
Welcome and Thank you classmate
 for taking part in our survey 

What's your name? 



