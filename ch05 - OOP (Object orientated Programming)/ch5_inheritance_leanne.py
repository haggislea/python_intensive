# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:49:52 2018

@author: leann
"""

##### animal game using classes ####       

class Animal():
    def __init__(self, name, age=0):
        self.name = name
class Dog(Animal):
    def __init__(self, name, age=0, barkNumber=0):
        self.barkNumber = barkNumber
        self.name = name
        
    def bark(self):
        print('Woof, woof! ')
        
class DogAgent(Dog):
    def detect(self):
        if self.barkNumber >=3:
            print('AAAAAAAAAA, Run! There\'s a stranger coming!!!!!! ')
        elif self.barkNumber == 0:
            print('You and {} are safe.'.format(name))
            
#class Robot():
#    def move(self):
#        print('I like to move it, move it')
#        
#class CleanRobot(Robot):
#    def clean(self):      
#            
#      
#        name = input("What is your pet\'s name?: ")
#        age = int(input("How old is {} ? ".format(name)))
#        bark = int(input("How many times have you heard {} bark?: ".format(name)))
#
#fluffy = DogAgent(name, age, bark)
#fluffy.bark()
#fluffy.detect()

"""
import sys    
    
class Animal():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def eat(self):
        print('yummy')
      
class Dog(Animal):     
    def bark(self):
        print('Woof!')
        
class Robot():
    def move(self):
            print('...move move move...')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum like I\'m hungry, dust is my food.')
        
class SuperRobot():
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog(name,age)
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark()
    def clean(self):
        return self.o3.clean()

name = sys.argv[1]
age = sys.argv[2]
print(name)
print(age)
   
#machineDog = SuperRobot()
#machineDog.move()
#machineDog.bark()

"""
    
    

class Monster():
    def __init__(self, name, age=0, scaleOfScariness=0):
        self.name = name
        self.age = age
        self.scaleOfScariness = scaleOfScariness
    
class Dinosaur(Monster):
    def __init__(self, name, age=0, scaleOfScariness=0):
        Monster.__init__(self, name, age, scaleOfScariness)
    
    def Run(self):
        if self.scaleOfScariness <= 5:
            print('This scariness level is low, but stay vigilant, stay alert. ')
            
        elif self.scaleOfScariness >=6 or self.scaleOfScariness <= 9:
            print('This is high on our monitor, be careful, very careful.....')
            
        elif self.scaleOfScariness == 10:
            print('Wow there people.  Is this {} even real or from a film?!!!  RUN!!'.format(self.name))
        else:
            print('error')
   
name = input("What type of monster are you dealing with?: ")
scaleOfScariness = int(input("On a scale of 1 to 10, how scary is this {}?  ".format(name)))
m1 = Dinosaur(name,0,scaleOfScariness)
m1.Run()

#
###### food order game using classes ####  
#        
#class Food():
#    def __init__(self, name, sauce):
#        self.name = name
#        self.sauce = sauce
#        
#               
#class Chips(Food):
#         
#    def __init__(self, name, sauce, portionSize):
#        self.portionSize = portionSize
#       
#        if self.portionSize >=6:       
#            print("I Love Carbs! \nFill me up ")
#
#            
#class Condiments(Food):
#    def __init__(self, name, sauce, portionSize):
#        self.sauce = sauce
#        
#    def sauce(self, condiments):
#        print ('WouLd you like Red or Brown sauce?')
#        if self.sauce == 'red':
#            print('Serving you up some big o\'l dollop of red sauce!')
#        elif self.sauce == 'brown':
#            print('yes sireeee, enjoy the sauce of excellence!')
#            
#            
#name = input("Hello, can I take your name?: ")
#print('Welcome to Chippery, {}.'.format(name))
#order = int(input('How many portions would you like?: '))
#sauce = input('Would you like red or brown sauce? ')
#customer = Chips(name, sauce, order)
