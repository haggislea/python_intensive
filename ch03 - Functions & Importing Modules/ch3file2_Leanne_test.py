# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:22:37 2018

@author: leann
"""

####
#  Functions & printing
####

hello_world() #calling the function

name = input("What's your name? ") 
print("Hello{} !".format(name).upper()) #makes tHe name upperase
print("Hello {} !".format(name).title()) #makes each word become a capital



eye_colour = input()
print("Your eye colour is {} !".format(eye_colour))
print('What is your eye colour?')

eye_colour = input("What is your eye colour?")
print("Your eye colour is {} !".format(eye_colour.upper())) #upper here will just do the eye colour, outside of the brackets will do whole sentence
print ("Hello {} ! She has {} eyes".format(name, eye_colour))



height = input()
print("Your are{}, no way! Wow!".format(height))
print("Your are{}, no way! Wow!".format(height))

height = input("How tall are you?")
print("You are {},no way?! Wow!".format(height))
print("How tall are you?")

name= input("What is your name? ")
eye_colour = input("What is your eye colour? ")
print ("Hello {} ! She has {} eyes".format(name, eye_colour))


print("You are {},no way?! Wow!".format(height))






####
#  Adding numbers & printing
####

print(add2_2)
your_name()
    
    
#----------------------------
#   Printing two added numbers together from arguments 
#----------------------------

print ("{} plus {} is {}".format(number, anotherNumber, answer))
add_two_numbers(11, 23)


#----------------------------
#   putting functions into practice
#----------------------------

print("Your pet is called {}! Your pet has a beautiful name!" .format(name))

print("What type of animal is your pet?")
print(" {}! That's such a great pet to have!".format(animal))
print("How old is your pet?")
print("WOW that is a hell of an age!")
print("Your pets is called {}. It is a {}, and is {}.".format(name, animal, age))
print (add) - took out s printing age twice






#--------------
#importing files can be done by via the import method

# In class task - converting temperature and distance
#--------------

import ch3_tempanddistance_function

ch3_tempanddistance_function.convert_temperature(45)
print('')

ch3_tempanddistance_function.convert_distance(20)
ch3_tempanddistance_function.convert_temperature(400.5)
ch3_tempanddistance_function.convert_temperature(28.8)
centigrade = 42

fahrenheit, kelvin = ch3_tempanddistance_function.temperature_conversion(centigrade)
print(fahrenheit, kelvin)
miles = 400

kilometers = ch3_tempanddistance_function.mileage_conversion(miles)
print("You have travelled {} miles,\ you are burning some fuel there!" .format(kilometers))
print("You will shortly run out of fuel!\nStop and pull over at your nearest petrol station")



