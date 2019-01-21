# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:28:20 2018

@author: leann
"""



#------    
# Chapter 12 - THE FOR LOOP
#-------
# Printing the contents of my shopping basket

my_shopping_cart = ['cake', 'plates', 'plastic forks', 'juice', 'cups']
for item in my_shopping_cart:
    print (item)

------     
prints out:
-------
    
cake
plates
plastic forks
juice
cups
    

 practising changing the 'name of the shopping list - make it relevant
    
    my_shopping_cart = ['cake', 'plates', 'plastic forks', 'juice', 'cups']
for gorilla in my_shopping_cart:
    print(gorilla)
    
    

#------    
# Updating list values
#-------

values = [875, 23, 451]
for val in values:
    print('---> '+str(val))
    
prints out:
---> 875
---> 23
---> 451
    
    for val in values:
        print('---> '+str(val+50))
        
        
 prints out:       
---> 875
---> 925
---> 73
---> 501
---> 23
---> 925
---> 73
---> 501
---> 451
---> 925
---> 73
 
 
 
# ------    
# lOOPING THROUGH OTHER TYPES
#-------
 prints the characters vertically on a separate line for each character of the word you want to print
 
for char in 'yes':
     print(char)
 y
 e
 s

for char in 'the titanic':
     print(char)
     
     #prints out:
t
h
e
 
t
i
t
a
n
i
c
 
 
for char in 'this', 'and', 'that' .split(' '):
    print(char)
 
  prints:
this
and
['that']
 
 
 
 
#----------
# Looping through a STRING
#----------- 
 
for char in ('what', 'will', 'the', 'weather', 'be', 'like', 'tomorrow?'):
    print(char)
what
will
the
weather
be
like
tomorrow?  

#----------
# Looping through a TUPLE
#----------- 

for char in(100, 99, 98 ,97, 96, 95):
    print(char)

#prints out:
100
99
98
97
96
95


#----------
# Operations within a FOR loop
#----------- 

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals = list(densities.keys())

metals

metals.sort(reverse=True, key=lambda m:densities[m])
metals



for metals in metals:
    print ('{0:>8} = {1:5.1f}'.format(metals, densities[metals]))
    
#prints out:
    gold =  19.3
    lead =  11.4
    iron =   7.8
    zinc =   7.1
    
    
for metals, value in densities.items():
    print ('{0:>8} = {1:5.1f}'.format(metals, value)) - 

prints out:
    iron =   7.8
    gold =  19.3
    zinc =   7.1
    lead =  11.4
 
 
# ----------
# Operations within a FOR loop  version 2
#----------- 
 

densities ={'iron':(7.8,100,11),'gold':(19.3, 20000, 9), 'zinc':(7.13, 40000,7), 'lead':(11.4, 80, 5)}

metals = list(densities.keys())
metals.sort(reverse=True, key=lambda m:densities[m])

keyValues = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)


for metals, metalValue in keyValues:
    print(metals,metalValue[1])
    
#prints out:
zinc 40000
gold 20000
iron 100
lead 80


# ----------
# Operations within a FOR loop  version 2 - changing value to '0'
#----------- 

for metals, metalValue in keyValues:
    print(metals,metalValue[0])

Prints out:

zinc 7.13
gold 19.3
iron 7.8
lead 11.4

# ----------
# Operations within a FOR loop  version 2 - changing value to '2'
#----------- 

for metals, metalValue in keyValues:
    print(metals,metalValue[2])
    
    ##Prints out:
zinc 7
gold 9
iron 11
lead 5


# ----------
# Operations within a FOR loop  version 2 - changing value to '0:0'
#----------- 

for metals, metalValue in keyValues:
    print(metals,metalValue[0:0])


zinc ()
gold ()
iron ()
lead ()


# ----------
# Operations within a FOR loop  version 2 - changing value to '0:0'
#----------- 

 
for metals, metalValue in keyValues:
    print(metals,metalValue[0:1])


#prints:
zinc (7.13,)
gold (19.3,)
iron (7.8,)
lead (11.4,)
 
 

# ----------
# combining IF, ELSE to filter out values
#-----------

densities ={'iron':(7.8,100,11),'gold':(19.3, 20000, 9), 'zinc':(7.13, 40000,7), 'lead':(11.4, 80, 5)}

metals = list(densities.keys())
metals.sort(reverse=True, key=lambda m:densities[m])

keyValues = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)


for metal in keyValues:
    if metal[1][0]>5:
        print(metal[0], '=', metal[1][0])
        print('There\'s some serious metal value here!')
    elif metal[1][0] <5:
        print(metal[0], '=', metal[1][0])
        print('hmm, this metal is not worth too much.\n Keep hold of it though,\nit may be woth more in the future')
    else:
        print(metal[0], 'This is kind of worth something, could improve with age.')
    
 
 
# ----------
# creating a christmas list
#-----------

 
Christmas_presents = {'car':10000, 'chocs':25, 'books': 100, 'holiday':25000}
loopRound = 1
for present, item in Christmas_presents.items():
    print('you\'ve opened the box'), loopRound, 'the gift is', item
    if item > 50:
        print('You are getting a good present from Father Christmas!')
    else:
        print('Sadly you were not very good this year.....')

    loopRound = 1




# ----------
# Designing a SUM FUNCTION
#-----------
## the TOTAL adds the first number then adds the values, it updates the values within the FOR LOOP
 

values = [3, 12, 9]
total = 0

for val in values:
    total += val
    print('TOTAL:' +str(total))
    
    ## prints out:
#TOTAL:3
#TOTAL:15
#TOTAL:24
  
    
def sumValues(l):
    sumV = 0
    for val in l:
        sumV += val
        return sumV
    print(sumValues(values))


# ----------
# LOOPS list with index
#-----------


list(range(10)) 

#prints out:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



values = [2, 4, 10]
#total = 0
#
for i in range(len(values)):
    values[i] = values[i] *2
    values
    
    ## prints out:
    [4, 8, 20]


values = [2, 4, 10]

for i in range (2, 4, 10):
    print(i)


list(range(2))
#prints out:
[0, 1]



#-------
#using different PARAMETERS
#-------


values = [2, 4, 10, 100, 250, 500]

for index in range(len(values)):

print(values[index])

### prints out:
2
4
10
100
250
500

#-------
#using different PARAMETERS
#-------

values = [2, 4, 10, 100, 250, 500]
for index in range(0,len(values),2):
print(values[index]

##prints
 2
10
250



#-------
#using break in FOR LOOPS
#-------


myList = [1,5,30,200,101,100,22]
for n in myList:
    if n > 100:
        print('Yep we are done here:', n)
        break
### if we do not use 'break' it prints out:
#prints out:
        Yep we are done here: 200

#-----------------------------------------------#


myList = [1,5,30,200,101,100,22]
for n in myList:
    if n > 100:
        print('Yep we are done here:', n)
        break
### if we use 'break' it prints out: 
#prints out:
Yep we are done here: 200
Yep we are done here: 101



#-----------------Another way of measuring how long the list is 
#                 and where it is breaking (at what point)------------------#
myList = [1,5,30,200,101,100,22]
for index in range(len(myList)):
    if myList[index] > 100:
        print('This is where it breaks:', myList[index], '\nwith the index point here: ', index)
        break
    
    
#prints out:
This is where it breaks: 200 
with the index point here:  3



##------------DICTIONARY COUNTER-------------

colour = ['red', 'blue', 'black', 'yellow']
d = {}

for item in colour:
    
    if item not in d:
        d[item] = 0
        print('first time we print ', d)
    else: 
        d[item] = d[item] + 1
        print(d)
##prints out:
        
first time we print  {'red': 0}
first time we print  {'red': 0, 'blue': 0}
first time we print  {'red': 0, 'blue': 0, 'black': 0}
first time we print  {'red': 0, 'blue': 0, 'black': 0, 'yellow': 0}


#-------
#   NESTED LOOPS
#-------

outer_vals = [1,2,3]
inner_vals = ['A','B','C']

for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)

## prints out:
1 A
1 B
1 C
2 A
2 B
2 C
3 A
3 B
3 C

#-------
#   NESTED LOOPS - prints each value out and then adds then together nd repeats through the string and list
#-------

outer_vals = [1,2,3]
inner_vals = ['A','B','C']
d={}
for oval in outer_vals:
    print(oval)
    for ival in inner_vals:
        print(ival)
        print(oval, ival)

##prints out:
1
A
1 A
B
1 B
C
1 C
2
A
2 A
B
2 B
C
2 C
3
A
3 A
B
3 B
C
3 C


#-------
#   NESTED LOOPS - alternative way
#-------


outer_vals = [1,2,3]
inner_vals = ['A','B','C']
d={}
for oval in outer_vals:
    print(oval)
    for ival in ['A','B','C']:
        d[oval] = ival
        print(d)

##prints out:
        
 1
{1: 'A'}
{1: 'B'}
{1: 'C'}
2
{1: 'C', 2: 'A'}
{1: 'C', 2: 'B'}
{1: 'C', 2: 'C'}
3
{1: 'C', 2: 'C', 3: 'A'}
{1: 'C', 2: 'C', 3: 'B'}
{1: 'C', 2: 'C', 3: 'C'}



#-------
#   NESTED LOOPS - my versions
#-------
      

innerHappy = [1,2,3,4,5]
outerHappy = ['Sad', 'Not Smiling', 'Mediocre', 'Okaydokey','Very Happy']
for ihappy in innerHappy:
    for ohappy in outerHappy:
        print(ihappy, ohappy)
 
    
  ## prints out:  
    
1 Sad
1 Not Smiling
1 Mediocre
1 Okaydokey
1 Very Happy
2 Sad
2 Not Smiling
2 Mediocre
2 Okaydokey
2 Very Happy
3 Sad
3 Not Smiling
3 Mediocre
3 Okaydokey
3 Very Happy
4 Sad
4 Not Smiling
4 Mediocre
4 Okaydokey
4 Very Happy
5 Sad
5 Not Smiling
5 Mediocre
5 Okaydokey
5 Very Happy



#-------
#   NESTED LOOPS - another version of printing out
#-------

innerHappy = [1,2,3,4,5]
outerHappy = ['Sad', 'Not Smiling', 'Mediocre', 'Okaydokey','Very Happy']
d={}
for ihappy in innerHappy:
    print(ihappy)
    for ohappy in outerHappy:
        print(ohappy, ihappy)    
        
        ####print:
 1
Sad 1
Not Smiling 1
Mediocre 1
Okaydokey 1
Very Happy 1
2
Sad 2
Not Smiling 2
Mediocre 2
Okaydokey 2
Very Happy 2
3
Sad 3
Not Smiling 3
Mediocre 3
Okaydokey 3
Very Happy 3
4
Sad 4
Not Smiling 4
Mediocre 4
Okaydokey 4
Very Happy 4
5
Sad 5
Not Smiling 5
Mediocre 5
Okaydokey 5
Very Happy 5


#-------
#   NESTED LOOPS - multiplication table
#-------


for i in range (1,7):
    for j in range(1,11):
        print('{0:>3}'.format(i * j), end='')
        print('\n')

## prints out:
      ###the first number on each list is working from numer 1 to number 11, doing the calcualtions fro 1, then 2, then 3, etc until it gets to 11 and STOPS!  
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 
  2
  4
  6
  8
 10
 12
 14
 16
 18
 20

  3
  6
  9
 12
 15
 18
 21
 24
 27
 30

  4
  8
 12
 16
 20
 24
 28
 32
 36
 40

  5
 10
 15
 20
 25
 30
 35
 40
 45
 50

  6
 12
 18
 24
 30
 36
 42
 48
 54
 60
 

##-------
##    multiplication table
##-------
 
 
 for i in range(1, 11):
    print( i, ":", end=" ")
    for j in range(1, 10):
        print("{:2d}".format(i * j), end=" ")
    print()
 
    ### prints out:
    
1 :  1  2  3  4  5  6  7  8  9 
2 :  2  4  6  8 10 12 14 16 18 
3 :  3  6  9 12 15 18 21 24 27 
4 :  4  8 12 16 20 24 28 32 36 
5 :  5 10 15 20 25 30 35 40 45 
6 :  6 12 18 24 30 36 42 48 54 
7 :  7 14 21 28 35 42 49 56 63 
8 :  8 16 24 32 40 48 56 64 72 
9 :  9 18 27 36 45 54 63 72 81 
10 : 10 20 30 40 50 60 70 80 90 
 
 
 
# #-------
##   BUBBLE SORTING!
##-------
# 
# values = [4, 3, 6, 5, 2, 1]
# N = len(values)
# for i in range(N-1):
#     if values[i] > values[i+1]:
#         tmp = values[i]
#
#values[i+1] = tmp
 
 

    
    
    
    
    
    
    
    