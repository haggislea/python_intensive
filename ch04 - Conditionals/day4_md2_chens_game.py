# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:46:57 2018

@author: leann
"""

import random
import datetime
import time

def luckyNumberRandom():
    name = input('To see into your mind, we need to connect.  What is your Name? ')
    print ("hello " + name.upper() )
    number = int(input('Select a number, any number, but dont say it aloud!'))
    
    print('your lucky number is.....'+ str(random.randint(1,number)))
      

startTime = time.time()
print('date and time', datetime.datetime.now())
print()
print('current time' , datetime.datetime.now().time())
luckyNumberRandom()
processTime = time.time()-startTime
print()
print('program running time:', round(processTime,2),'second')    




def DataBundlePurchase(self, truePasscode, balance):
    truePasscode = input('Please enter your password: ')
    print('Your password is correct)')
    self.balance = blance