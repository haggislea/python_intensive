# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:13:43 2018

@author: leann
"""


#### Number games using IF, ELIF and ELSE   #####

number = input("Enter a number betwwen 1 and 10:")
number = int(number)  #converts the string into an integer

if number > 10:
    print("To high!!!  Have another go....")

elif number <0:
    print("Too low!! Come, on have another go.....")

elif number <10:
    print("That\'s a fine number to choose!")

else:
    print('Our work here is done')

""" 
number = input("Enter a number between 1 and 10:")
number = int(number) 

if number >10:
    print("Too high")
    
else:
    print("Too low")    



#####  Altitude Game using IF, ELIF and ELSE  ####

warning = input("What is your current altitude?: ")
altitude = int(warning) 

if 0 < altitude <= 200:
    print("Nice knowing you my friend.......")
    
elif altitude <1000:
    print("WARNING!")
    print("Time to bail out, my friend, life is worth living")
    
elif altitude <5000:
    print("Try climbing to a higher height")
    
  
elif altitude <40000:
    print("You're doing fine. A sterling job. Stay safe my fellow flier of the sky")

else:
    print("WOW there space ship enterprise,\nyou'll be exiting Planet Earth soon!")
    print("Decrease your altitude NOW, my little star traveller")


####### Planet Earth game    #########

print('State your name earthling: ')
name = input()

print('How many earthling years are you?')
age = input()

print("hello {} you\'ve reached BT space center. Because you\'ve reached the grand old age of {}".format(name,age) + "you have qualified to escaped this doomed planet") 

time = int(input("So young creature, pick a number, any number  and we\'ll decide your fate in this Galaxy: ")) 


if 0 < time <= 10:
    print("Off to Mars you shall go!")
    print('Be aware that this planet disappeared over the course of hundreds of millions of years')
    print('.....better pack some goodies, as we may not see you again')
    
elif 11 <= time <= 20:
    print("WARNING! You are off to Jupiter")
    print("There is no single person credited with discovering this planet")
    print()
    print('patent it and it\'s all yours!')
     
elif 21 <= time <= 30:
    print("Saturn here you come!")
    print('A day on Saturn is only ten hours and forteen minutes long')
    print()
    print('No daylight savings here!!')
    
  
elif 31 <= time <= 40:
    print("Uranus is your destiantion my little earthling")
    print('Your new home takes a trip around the Sun EVERY eighty four (Earth) years!!')
    print()
    print('Don\'t forget to book your sun bed before you leave ')

elif 41 <= time <= 50:
    print('Neptune, here you come') 
    print('This planet is super cold')
    print()
    print('Pack an extra blanket!')
    
elif 51 <= time <= 60:
    print('Mercury here you come traveller')
    print()
    print('It is almost sixty million kilometres away....still sure on going?!')
    
elif 61 <= time <= 70:
    print('Planet Venus is your destination')
    print('Did you know the atmosphere is hot and thick?')
    print()
    print('If you are looking for something tropical, this is your place')
    
elif 71 <= time <= 80:
    print('Would you look at that? Guess your time\'s up luv')
    print()
    print('It\'s a shame you couldn\'nt live up to your life expectancy')


else:
    print("Unfortunately you\'ve missed your planet. Please dial again later and an operator will be with you shortly")
    print("Don\'t give up my little star traveller, we haven\'t made any cuts to this service just yet")
    
    
    ##### Using imports, defining functions to play a game#


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



        