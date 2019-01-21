# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:16:32 2018

@author: leann
"""



##   WARM UP 1 --- SLEEP IN
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else: 
    return False

##    WARM UP 1

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b< 0))

####  WARM UP --- DIFF 21

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

####  WARM UP ---front back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  return str[len(str)-1] + mid + str[0]

####  WARM UP --- monkeys smiling
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
return False

###  WARM UP --- stringy thing
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

####  WARM UP  > near_hundred ---
  
def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
  

####  WARM UP ---  >  missing_char#
  def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back  


####  WARM UP > front 3---
def front3(str):
  if len(str) < 3:
    return str * 3
  return str[:3] * 3

####  WARM UP > parrot trouble
  def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

####  WARM UP >sum double
  def sum_double(a, b):
  if a == b:
    return a * 4
  return a + b

####  WARM UP >makes 10
  def makes10(a, b):
  return a + b == 10 or a == 10 or b == 10

####  WARM UP >
