# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:07:27 2018

@author: leann
"""

######### The world of Lists and Tuples ##########

#mutable = can be changed
#immutable = cannot be changed
#tuples = use () brackets are immutable, a group fo datat, an ordered sequence of events that are uncahngeable, whose values can't be modified
#lists use [] and are mutable, allows you to store and track information


a = ['Tiger', 'PPolar  Bear', 'Lion',  'Giraffe', 'Dolphin']
sorted(a)
a
sorted(a)
 #prints this      ['Dolphin', 'Giraffe', 'Lion', 'PPolar  Bear', 'Tiger']


sorted(a, reverse=True)
prints this      ['Tiger', 'PPolar  Bear', 'Lion', 'Giraffe', 'Dolphin']

w = ['99','98', '97', '96', '95', '94', '100']
sorted(w)
 prints this     ['100', '94', '95', '96', '97', '98', '99']

w[-1] = 500

w
prints this     ['99', '98', '96', '95', '94', 500]

w[1:4]
prints this   ['98', '96', '95']

w[0:3:1]
prints this out    ['99', '98', '96']


my_favourite_fruits = ['apple,', 'orange','banana']
x = ['this', 55, 'that', my_favourite_fruits]
x[0]
#prints
'this'

x[7]
prints 
Traceback (most recent call last):

  File "<ipython-input-160-1515eb8c000f>", line 1, in <module>
    x[7]

IndexError: list index out of range


my_favourite_fruits = ['apple', 'banana', 'kiwi', 'pineapple', 'orange', 'satsuma']
#print (my_favourite_fruits[4])
#
#
prints
['this', 55, 'that', 'carrot']

list
x[1] = 'and'
x

##print['this', 55, 'that']

x[1] = 'and'

x
print['this', 'and', 'that']

x.append('again')

x
print['this', 'and', 'that', 'again']


x = ['the', 'cat', 'sat']

y = ['being', 'lazy' ,'was', 'its', 'life', 'ambition']

z= x + y

z
print['the', 'cat', 'sat', 'being', 'lazy', 'was', 'its', 'life', 'ambition']

set(x + y)
prints     {'ambition', 'being', 'cat', 'its', 'lazy', 'life', 'sat', 'the', 'was'}


x = [7,11,3,9,2]
y = sorted(x)
#
#

#####Tuples
deal = [25, 50,75]
del deal [-2]

prints    [25, 75]

a = [0,1,2,3,4,5,6,7,8,9]
del a[-1]
a
prints [0, 1, 2, 3, 4, 5, 6, 7, 8]

a = [0,1,2,3,4,5,6,7,8,9]
a[0] = 50
a
print [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.append('z')
a

squire = ['cow', 'pig', 'chicken']
squire.append('goat')
squire
print     ['cow', 'pig', 'chicken', 'goat']




meal_order = ['glass of red wine', 'pepperone pizza', 'side of salad', 'olives', 'bruschetta' ]
meal_order.append('slice of choclate cake')
meal_order
prints

['glass of red wine',
 'pepperone pizza',
 'side of salad',
 'olives',
 'bruschetta',
 'slice of choclate cake']



print [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'z']
#
#
#
x2 = [('a', 3), ('c', 1), ('b', 5)]
sorted(x2)
##prints  [('a', 3), ('b', 5), ('c', 1)]
#
# 

###slicing###
x[1:4]

prints    ['and', 'that', 'bits']

it is starting at 1, which is 'and' and stops at four, but does not include it, effectively it just is saying, take 1,2,3.

using minus numbers, these never include starting at zero and always starts from teh right side
x[-2]
prints x[-2]

x[1:-2]
prints   ['and', 'that', 'bits']


sorted(l)
x = [7,3,11,21]
y = sorted(x)
print(y)

sorted(x)
print(y)

sorted(x,reverse=True)
prints it in reverse   [21, 11, 7, 3]

l.sort():
    
x = [7,3,11,21]
x.sort()
x
prints    [3, 7, 11, 21]
x
prints     [21, 11, 7, 3]
 x.sort(reverse=False)
 x
prints    [3, 7, 11, 21]

x = ['a','b','c','d','e','f']
sorted(x)
prints     ['a', 'b', 'c', 'd', 'e', 'f'] 


chens example

x = []
y = sorted(x)
#print(now x is: ', x)
#print(now y is: ', y)
#print()

--------

x.sort
y=x.sort()
print(now x is: ', x)
print(now y is: ', y)
print()
#


bob = ['I', 'am', 'very', 'lazy']
sorted(bob)

prints     ['I', 'am', 'lazy', 'very']





#------------generic sorted() function---------------
now x is: ['ab', 'cs', 'yw', 'zs', 'hd']
now y is: ['zs','yw', 'hd', 'cs', 'ab']

#------------object.method .sort---------------
now x is: ['zs','yw', 'hd', 'cs', 'ab']
now y is: None
F

#Lambda practice####

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]

x = ['Pete', 'Janet', 'Mutil', 'Girogio', 'Madge', 'Zebidiah']
y = ['Duck', 'Turkey', 'Emu', 'Parrot', 'Swan', 'Goose']
z = ['Stripe', 'plain', 'dotted', 'spotted', 'diagonals', 'horizontal']

y=sorted(x)
x2 = [('a', 3, z), ('c', 1, y) ,('b',5,x)]
print(sorted(x2, key =lambda s:s[2]))

#prints out
[('c', 1, ['Girogio', 'Janet', 'Madge', 'Mutil', 'Pete', 'Zebidiah']), 
('b', 5, ['Pete', 'Janet', 'Mutil', 'Girogio', 'Madge', 'Zebidiah']), 
('a', 3, ['Stripe', 'plain', 'dotted', 'spotted', 'diagonals', 'horizontal'])]

employees = [('Janine Saunders', 50000, 'UX Designer'),
     ('Robert Webster', 90000, 'Senior Engineer'),
     ('Jack Murning', 40000, 'Junior Web Developer'),
     ('Jen Burns', 30000, 'Content Creator'), 
     ('Hannah Beth', 40000, 'Communications Specialist')]
    
print (sorted(employees, key = lambda salary:salary[2]))

prints out
[('Hannah Beth', 40000, 'Communications Specialist'), 
 ('Jen Burns', 30000, 'Content Creator'),
 ('Jack Murning', 40000, 'Junior Web Developer'),
 ('Robert Webster', 90000, 'Senior Engineer'),
 ('Janine Saunders', 50000, 'UX Designer')]

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

x2 = [('a', 3, z), ('c', 1, y) ,('b',5,x)]

print(sorted(x2, key =lambda s:s[2][1]))
#prints out    
[('c', 1, ['aa', 'ed', 'fy', 'hw', 'lf', 'sb']), 
 ('b', 5, ['aa', 'sb', 'lf', 'hw', 'ed', 'fy']), 
 ('a', 3, ['fg', 'uj', 'sx', 'uj', 'ww', 'cf'])]

x = [1,2,3,4]

y = [3,4,10,3]

z = [10,20,30,40]

y[0]='zz'
#x2 = [('a', 3, z), ('c', 1, y) ,('b',5,x)]

sorted(x2, key =lambda s:s[2])
#prints out 
 [('b', 5, [1, 2, 3, 4]), ('c', 1, [3, 4, 10, 3]), ('a', 3, [10, 20, 30, 40])]






sorted(x2)

prints

[('a', 3, ['fg', 'uj', 'sx', 'uj', 'ww', 'cf']),
 ('b', 5, ['xa', 'sb', 'lf', 'hw', 'ed', 'fy']),
 ('c', 1, ['ed', 'fy', 'hw', 'lf', 'sb', 'xa'])]

sorted(x2, key=lambda s:s[1])
prints
[('c', 1, ['ed', 'fy', 'hw', 'lf', 'sb', 'xa']),
 ('a', 3, ['fg', 'uj', 'sx', 'uj', 'ww', 'cf']),
 ('b', 5, ['xa', 'sb', 'lf', 'hw', 'ed', 'fy'])]
















