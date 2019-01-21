# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:23:44 2018

@author: leann
"""

#        queens_age = 92
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