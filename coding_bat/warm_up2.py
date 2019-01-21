# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 19:19:55 2019

@author: leann
"""

#-----
# warm up 2
#-----  

#  string times
def string_times(str, n):
  return str * n

#  string splosion
def string_splosion(str):
  result = ''
  for n in range(0,len(str)+1):
    result += str[:n]
  return result  

#  array front 9
def array_front9(nums):
  for element in nums[:4]:
    if element == 9:
      return True
  return False

#  front times
def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[:3] * n

#  last2
def last2(str):    
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1  
  return count

#   array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

#  string bits
def string_bits(str):
  result = ''
  for n in range(0, len(str)):
    if n%2 == 0:
      result += str[n]
  return result

#  string match
def string_match(a, b):
  min_length = min(len(a), len(b))
   
  count = 0 
  for i in range(min_length-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count