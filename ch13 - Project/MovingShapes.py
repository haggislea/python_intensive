# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:43:42 2018

@author: leann
"""
     

from Shapes import *

from pylab import random as r

class MovingShape:
    def __init__(self,frame,shape,diameter):
#    def __init__(self,frame,shape,diameter, fillcolor):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        
#        self.fillcolor = fillcolor
#       self.frame = frame
        
#----
# setting the min and max plus the dimensions of the frame object attributes (width & height)
#----  
        
        self.minx = self.diameter
        self.mini = self.diameter
        
#        self.maxx = self.diameter
#        self.maxi = self.diameter
        
        self.maxx = frame.width - self.diameter
        self.maxi = frame.height - self.diameter
        

#----
# this adds the randomness
#----        
        self.x = self.minx + (r() * (self.maxx - self.minx))
        self.y= self.mini + (r() * (self.maxi - self.mini))
        
#------
#   if using this all shapes will move in  poitive diretion, once they ht the wall they disperse randomly   
#-----
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()

        
          
#----
# positioning the shape at point 'x' to 'y'
#----
                  
    def goto(self,x,y):
        self.figure.goto(x,y)
#        self.x = (0,0)
#        self.y = (0,0)
            
    def moveTick(self):
#----
# the moves
#----
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy 
        
        self.x = self.x
        self.y = self.y
 
        if self.x >= self.maxx :
            self.dx = self.dx * -1 
    
        elif self.y >= self.maxi:
            self.dy = self.dy *-1
            
        elif self.x <= self.minx :
            self.dx = self.dx * -1 
    
        elif self.y <= self.mini:
            self.dy = self.dy *-1
            
#        else:
#            False
#           print('This appears not to be working')
#    
            
        self.goto(self.x, self.y)
        
#-------
# if wanting to split out the 'self.dx' and 'self.dy' and define the function of randomness these functions are valid
#-----
#def MoveX(self):
#        self.dx = 5 + 10 * r()
#        if r() > 0.5:
#            self.dx = self.dx
#        return self.dx
#   
#def MoveY(self):
#        self.dy = 5 + 10 * r()
#        if r() > 0.5:
#            self.dy = self.dy
#        return self.dy
        

class Square(MovingShape):
    def __init__(self,frame,diameter):
#    def __init__(self,frame,diameter, fillcolor):
        MovingShape.__init__(self,frame,'square',diameter)
        
        self.minx = self.diameter/2
        self.mini = self.diameter/2
        
#        self.fillcolor('green')
#        self.begin_fill()

    
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
#    def __init__(self,frame,diameter, fillcolor):
        MovingShape.__init__(self,frame,'diamond',diameter)
#----
# the diamonds width and height becomes much greater when a square is moved to 45 degrees (it becomes a diamond shape), to rectify the problem of the diamond not moving the diameter of the square (d2), is thus d2 = 2*d1, this allows the calculations for the dimond to now move as base don just d2 it would not
#----       
        self.diameter =2 *self.diameter
        self.minx = self.diameter/2
        self.mini = self.diameter/2
        
#        self.fillcolor('orange')
#        self.begin_fill()
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
#    def __init__(self,frame,diameter, fillcolor):
        MovingShape.__init__(self,frame,'circle',diameter)
        
#        self.fillcolor('red')
#        self.begin_fill()
        
# other shapes that could be added but needs more coding work to include the tutrtle.py file too    

#class Star(MovingShape):
#    def __init__(self,frame,diameter):
#        MovingShape.__init__(self,frame, 'star', diameter)  
#        self.minx = self.diameter/2
#        self.mini = self.diameter/2
        
#class Cross(MovingShape):
#    def __init__(self,frame,diameter):
#        MovingShape.__init__(self,frame, 'cross', diameter)  

#class Pentagon(MovingShape):
#    def __init__(self,frame,diameter):
#        MovingShape.__init__(self,frame,'pentagon',diameter)
#
#        self.diameter =2 *self.diameter
#        self.minx = self.diameter/2
#        self.mini = self.diameter/2

#-----
# thoughts and workings outs
#-----
        
        
#        x frame.height == self.maxx
#        x frame.width == self.minx
#        
#        if x frame.height => d2:
#            return True
#        else:
#            False
#            
#        if x frame.width <= -d2:
#            return True
#        else:
#            False           
#
#        
#        self.x min value == self.minx
#        if (x min value => d2 == self.minx):
#            return True
#        else:
#            False
#                   
#        y max value == self.maxx
#
#        if y max value <= -d2 == self.maxx:
#            return True
#        else:
#            False
        