# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:28:19 2018

@author: leann
"""


from Shapes import *    

frame = Frame()
s1 = Shape('square', 50)
s1.goto(200,100)

s2 = Shape('circle', 75)
s2.goto(100,125)

s3 = Shape('diamond', 75)
s3.goto(55,75)

#s4 = Shape('star', 100)
#s4.goto(100, 100)

x = 0
y = 0

for i in range(100):
    s1.goto(x,y)
    x = x + 3
    y = y + 3
    
for i in range(100):
    s2.goto(x,y)
    x = x + 2
    y = y + 2  

for i in range(20):
    s3.goto(x,y)
    x = x + 1
    y = y + 1  
    
#frame.close()      this closes the windows