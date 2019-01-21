# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:15:26 2018

@author: leann
"""

from MovingShapes import *

frame = Frame()
numshapes = 4  ##the number of shapes present within the walls
shapes = []
size = 25  ##the size of the actual shape

#---
# adds the shapes needed
#---

for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
#    shapes.append(Star(frame,size))
#    shapes.append(Cross(frame,size))
#    shapes.append(Pentagon(frame,size))


#---
# moves the shapes around
#---

for i in range(100):
    for shape in shapes:
        shape.moveTick()
        

        
    