# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:40:35 2019

@author: leann
"""

###Warm up string 1

# hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make out word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#first half
def first_half(str):
  return str[:len(str)/2]

#non start
def non_start(a, b):
  return a[1:] + b[1:]  

#make abba
def make_abba(a, b):
  return a + b + b + a

#extra end
def extra_end(str):
  return str[-2:] * 3

#eithout end
def without_end(str):
  return str[1:-1]

#left 2
def left2(str):
  return str[2:] + str[:2]  

#make tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

#first two
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]

#combo string
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a