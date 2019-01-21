# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:07:21 2018

@author: leann
"""

#----
#Revising OOP
#---


###The syntax of defininf a class

class Person:
    def __init__(self):
        self.name = None
        self.age = 'not definied'
        self.isMale = None
##prints out:
p1 = Person()
p1.age 
'not definied'    
        
        
#---- the iniit is called to intitialise the object, which is p1, the statement of age is then added to this and the value is dislplayed, currently as not definied.


#----
# initiliasing the Person class
#----

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else: print('Gender is not known')
   
##input:
        
#p1 = Person('Janey', 78, 'f')
#p1.name
#p1.ge
#p1.isMale

##prints out:

#'Janey'
#78
#False 

     
#----
#Adding functionality
#----        
        
def greetingInformal(self):
        print('Hello there', self.name)
def greetingFormal(self):
        if self.isMale:
            print('Welcome there, Mr ',self.name)
        else: 
            print('Welcome there, Ms ',self.name)

#---
#adding a greeting
#---
def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome young ', self.name)
        elif self.age >60:
            print('Welcome venerable ', self.name)
        else:
            self.greetingFormal()
            
#---
#adding another CLass
#---
            
class Wizard(Person):
    def greetingFormal(self):
        print('Welcome, Mr ', self.name, end='')
        print('- you\'re a fine wizard!')
        
        
#---
# REDEFINING THE  __init__ subclass
#---        
        
class Wizard(Person):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.isMale = True
     
#---
# A NEW __init_ method
#---   
class Wizard(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm')     
        
#this is where the person __init__ superclass is invoked like so:         
Person.__init__(self,name,age,'m')
        
 
#---
# ADDING NEW Methods to wiard class
#---       
        
class Wizard(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm')  
        
        
        
    def spell(self):
        print('Expelliarmus! And that\'s it folks!)
        
        
    def magic(self):
        print('Would you like to see some magic?')
        if letsPlay == 'yes':
            self.wantsMagic = True
        elif letsPlay == 'no':
            self.wantsMagic = False
            Print('No magic games for you today, how sad.')
        else:
            prints('We\'ve run out of magic today, please return tomorrow.')
        

        
