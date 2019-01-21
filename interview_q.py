# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#-------
#version 1
#-------


import string
alphabet = string.ascii_uppercase

for i in range(0, len(alphabet)):
    if i % 3 ==2 and i % 4 ==3:
        print(str(i+1)+alphabet[i].lower())
        
    elif i % 3 == 2:
            print(alphabet [i].lower())
            
    elif i % 4 ==3:
            print(i+1)
    else:
        print(alphabet[i].upper())


  
##-----
## 2nd version
##----    
#    
#alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
#
#for letter in alphabet:
#    print(letter.upper())
#    
##alphabet[::3]
#
### prints out:
##['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y']   
##    