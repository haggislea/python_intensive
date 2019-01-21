# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:11:42 2018

@author: leann
"""

class Universe ():
    
    def __init__(self,name,time,age):
        #This class contains 3 objects'
        self.name = name
        self.age = age
        self.time = int(time) 

class Galaxy (Universe):
    def __init__(self,name,time,age,planetNumber=0):
        Universe.__init__(self,name,time,age)
        self.planetNumber = planetNumber
        
        
      
    def travel(self):
        print('All calls are monitored to improve customer service')
        
        
    def flying(self):
        print(self.time)
        if 0 < self.time <= 10:
            print("Off to Mars you shall go!")
            print('Be aware that this planet disappeared over the course of hundreds of millions of years')
            print('.....better pack some goodies, as we may not see you again')
        
        
        elif  11 <= self.time <= 20:
            print("WARNING! You are off to Jupiter")
            print("There is no single person credited with discovering this planet")
            print()
            print('patent it and it\'s all yours!') 
     
 
        elif  21 <= self.time <= 30:
            print("Saturn here you come!") 
            print('A day on Saturn is only ten hours and forteen minutes long')
            print()
            print('No daylight savings here!!')
    

        elif  31 <= self.time <= 40:
            print("Uranus is your destiantion my little earthling")
            print('Your new home takes a trip around the Sun EVERY eighty four (Earth) years!!')
            print()
            print('Don\'t forget to book your sun bed before you leave ')


        elif 41 <= self.time <= 50:
            print('Neptune, here you come') 
            print('This planet is super cold')
            print()
            print('Pack an extra blanket!')
    

        elif  51 <= self.time <= 60:
            print('Mercury here you come traveller')
            print()
            print('It is almost sixty million kilometres away....still sure on going?!')
    
        elif  61 <= self.time <= 70:
            print('Planet Venus is your destination')
            print('Did you know the atmosphere is hot and thick?')
            print()
            print('If you are looking for something tropical, this is your place')
        

        elif 71 <= self.time <= 80:
            print('Would you look at that? Guess your time\'s up luv')
            print()
            print('It\'s a shame you couldn\'nt live up to your life expectancy')
    
        elif self.time > 80:
            print("Unfortunately you\'ve missed your planet. Please dial again later and an operator will be with you shortly")
            print("Don\'t give up my little star traveller, we haven\'t made any cuts to this service just yet")
            
        else: 
            print("invalid value. Please ensure you enter a number above zero")

print('State your name earthling: ')
name = input()
print()

print('How many earthling years are you?')
age = input()
print()

print("hello {} you\'ve reached BT space center. Because you\'ve reached the grand old age of {}".format(name,age) + " you have qualified to escaped this doomed planet") 

time = int(input("So young creature, pick a number, any number and we\'ll decide your fate in this Galaxy: ")) 




Amina = Galaxy(name, age, time, 0)
#Amina = destination(Galaxy)
Amina.flying()
Amina.travel()

