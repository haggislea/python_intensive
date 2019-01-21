# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:57:01 2018

@author: leann
"""
####
# INPUT FROM A USER
####

#input functions
#--------------

#---------
# Printing an answer
#--------
#
#name = input("What's your name? ") 
#print("Hello{} !".format(name).upper()) #makes tHe name upperase
#
##print("Hello {} !".format(name).title()) #makes each word become a capital
#
#
##print('What is your eye colour?')
#eye_colour = input()
##print("Your eye colour is {} !".format(eye_colour))
#
#eye_colour = input("What is your eye colour?")
##print("Your eye colour is {} !".format(eye_colour.upper())) # upper here will just do the eye colour, outside of the brackets will do whole sentence
#
#
##print("How tall are you?")
#height = input()
##print("Your are{}, no way! Wow!".format(height))
#
#height = input("How tall are you?")
##print("You are {},no way?! Wow!".format(height))
#
#name= input("What is your name? ")
#eye_colour = input("What is your eye colour? ")
##print ("Hello {} ! She has {} eyes".format(name, eye_colour))
#

def hello_world(): #defining your function
        #print("Hello World!") #what gets pritned out
#hello_world() #calling the function
        


###### 
#function where 2 numbers can be added together-------  #########

def add(a,b):
    return print(a+b)


#####
#  ADDING TWO NUMBERS TOGETHER
######

    
def addition():
    add2_2=2+2
    #print(add2_2)
#your_name()



#----------------------------
#   adding two numbers from arguments
#----------------------------


def add_two_numbers(number, anotherNumber):
    answer = number + anotherNumber
#    print ("{} plus {} is {}".format(number, anotherNumber, answer))
#add_two_numbers(11, 23)



#----------------------------
#   putting functions into practice
#----------------------------


def all():
        #print("What is your pets name?")
        name = input()
    
        #print("Your pet is called {}! Your pet has a beautiful name!" .format(name))
      
       
    
        #print("What type of animal is your pet?")
        animal = input()
    
#        print(" {}! That's such a great pet to have!".format(animal))
    
    
        #print("How old is your pet?")
        age= int(input())
                
        #print("WOW that is a hell of an age!")
        
        #print("Your pets is called {}. It is a {}, and is {}.".format(name, animal, age))
   
        add = age*7
#        print (add) - took out s printing age twice
        print("In human years your pet is {} years old".format(add))
       
#all()


#----------------------------
#FUNCTION PRACTICE
#----------------------------


def convert_distance(miles):
    kilometers = (miles * 8.0) /5.0
    print("Converting distance in miles to kilometers.")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)



def convert_temperature(centigrade):
    fahrenheit = (centigrade * 9.0/5.0) + 32
    kelvin = centigrade + 273.15
    print("Converting temperature in centigrade to Fahrenheit or Kelvin.")
    print("Temperature in fahrenheit:", fahrenheit)
    print("Temperature in kelvin:", kelvin)


def convert_temperature(centigrade):
    fahrenheit = (centigrade * 9.0/5.0) + 32
    print("Your temperture is {}.".format(fahrenheit))


def temperature_conversion(centigrade):
    fahrenheit = (centigrade * 9.0/5.0) + 32
    kelvin = centigrade + 273.15
    return(fahrenheit, kelvin)



def mileage_conversion(miles):
     kilometers = (miles * 8.0) /5.0
     return(kilometers)
     









