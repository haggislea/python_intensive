# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:36:58 2018

@author: leann
"""

#####  LOGIC ----squirrels play
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90

##first attempt
def squirrel_play(temp, is_summer):
  if temp <= 60:
    return False
    elif temp =>90:
      return False
  return True
  

####### love6
def love6(a, b):
  return 6 in [a, b, a + b, abs(a - b)]

####didnt work
def love6(a, b):
  if a == 6 or b ==6 or (a + b) == 6 or abs(a - b) == 6:
    return True


#####if not outside

##my attempt:
#def in1to10(n, outside_mode):
  if n >1 or <10:
    return True
  else:
    n <=1 or =>10
    return False
  
def in1to10(n, outside_mode):
  if not outside_mode:
    return n in range(1, 11)
  return n <= 1 or n >= 10

# cigar party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

# caught speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
     
  if speed <= 60:
      return 0
  if 60 < speed <= 80:
    return 1
  return 2
 
# date fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  return 1

# sorta sum
def sorta_sum(a, b):
  if 10 <= a + b < 20:
    return 20
  return a + b

# alarm clock
def alarm_clock(day, vacation):
  if not vacation:
    if 1 <= day <= 5:
      return '7:00'
    return '10:00'
  
  if 1 <= day <= 5:
    return '10:00'
  return 'off'

#near ten
def near_ten(num):
 return num % 10 in [0,1,2,8,9,10]








