# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:56:18 2018

@author: leann
"""

####  Module 2 - Chapter 7  -  Debugging####

#The code below was used to be aware of and know how to use the break point and debugging within Python.
#using the print function allows you you to see where the possible error is occuring

#userInput = input('Pleaase give a number ')

#result = userInput - 2

#print(type(userInput))

#result2=int(userInput-2)

##prints an error

#print(result2)


######      Spyder Debugging   ##################
#along the top of the screen are some blue icons which allow you to move through the code. (They are icons of what they can do)
#1. double click on a numbered line to add a point called debugging(a debugging point)
#2. 1st button (play, pause), will run the code until the first break point. ( break point is red coloured dot on the numbered line)
#3. 2nd button will run the code line by line
#4. 3rd button goes into the function (or known as steps into the function)
#5. 4th button will run into the next function or method returns
#6. 5th button will run until the next break point (looks like a fast forwrd button!)
#7. 6th button will stop the debugging happening (blue square button)



######   ---  Spyder Debugging Example ---- #####

userInput = input('Please give a number ')
print(type(userInput))
#prints 
Please give a number 5
<class 'str'>

userInput = input('Please provide me with a number: ')
def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput -2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

##prints  
#Please give a number 2
#0

###### debugging ######





