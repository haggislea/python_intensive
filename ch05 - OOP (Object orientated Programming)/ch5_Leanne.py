## -*- coding: utf-8 -*-
#"""
#Created on Wed Dec  5 08:42:30 2018
#
#@author: leann


#### Module 2 - OOP (Object Orientated Programming) #######

###  Using classes, how to apply for encapsualtion, 
##inheritance, interfaces and association #######

"""A customer of ABC Bank with a checking account.
 Customers have the following properties:
 Attributes:
 name: A string representing the customer's name.
 balance: A float tracking the current balance of the
 customer's account.
 """
 
 
#-----------------
 #TASK 1
#----------------

class Customer(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance 
  
def withdraw(self, amount):  
    
        if amount>self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance-=amount
        return self.balance
        
def deposit(self, amount):
    self.balance += amount
    return self.balance 

jason = Customer('Jason Taylor', 1000.0)


#-----------------
 #TASK 2, 3 and 4
#----------------

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Dog(Animal):
    def __init__(self, name, age, barkNumber):
        self.barkNumber = barkNumber
        self.name = name
        
    def bark(self):
        print('Woof, woof! ')
        
class Cat(Animal):
    def __init__(self,name,age):
      Animal.__init__(self,name,age)
    def Meow(self):
        print('Meow')

fluffy = Dog('flufster', 5, 'sheepdog')
print('fluffy.name')
fluffy.bark()
fluffy.detect()

#--------------   Task 3---------

class Animal():
    def eat(self):
        print("yum")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class Robot():
    def move(self):
        print("... move move move, I like to MOVE IT!...")

class CleanRobot(Robot):
    def clean(self):
        print("I vacuum dust, I love Dust!")
        


class SuperRobot():
    
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
        
    def move(self):
        return self.o1.move() 
    
    def bark(self):
        return self.o2.bark() 
    
    def clean(self):
        return self.o3.clean() 
    
    
machineDog = SuperRobot()
machineDog.move()
machineDog.bark()
machineDog.clean()




##  Task 4 -- Robot game using classes  ###

class Robot():
    def move(self):
        print('I like to move it, move it')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum like I\'m hungry, dust is my food.')
        
class CookRobot(Robot):
    def cook(self):
        print('I make chocolate cake, good chocolate cake, the BEST!')
        
me = CleanRobot()
me.clean()

me = CookRobot()
me.cook()

me = Robot()
me.move()
me.move()
me.move()
me.move()
me.move()

me = CookRobot()
me.cook()



#------##### OWN WORK: extras for practice #####
####  Using classes  ###

class Vegetable():
    def eat(self):
        print('hmmmm yummy!')

class Carrot(Vegetable):
    def crunchy(self):
        print('I do love crunchy carrots')

me = Carrot()
me.crunchy()
me.eat()


#------##### OWN WORK: extras for practice #####
#### food order game using classes ####  
        
class Food():
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        
               
class Chips(Food):
         
    def __init__(self, name, sauce, portionSize):
        self.portionSize = portionSize
       
        if self.portionSize >=6:       
            print("You love your Love Carbs! ")

            
class Condiments(Food):
    def __init__(self, name, sauce, portionSize):
        self.sauce = sauce
        
    def sauce(self, condiments):
        print ('WouLd you like Red or Brown sauce?')
        if self.sauce == 'red':
            print('Serving you up some big o\'l dollop of red sauce!')
        elif self.sauce == 'brown':
            print('yes sireeee, enjoy the sauce of excellence!')
            
            
name = input("Hello, can I take your name?: ")
order = int(input('How many portions of chips would you like?: '))
sauce = input('Would you like red or brown sauce? ')
customer = Chips(name, sauce, order)

#------##### OWN WORK:  Scary Monster game ####

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
