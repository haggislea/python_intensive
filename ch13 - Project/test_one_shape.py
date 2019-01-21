# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:53:16 2018

@author: leann
"""

from MovingShapes import *
frame = Frame()
shape1 = Square(frame,100)
for i in range(100):
    shape1.moveTick()
    

