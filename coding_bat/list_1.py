# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 19:01:09 2019

@author: leann
"""


#-----
#list - 1
#-----


# first last6
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

# common end
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

# reverse 3
def reverse3(nums):
  return nums[::-1]

# middle way
# same first last
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

# sum3
def sum3(nums):
  return sum(nums)

# max end 3
def max_end3(nums):
  m = max(nums[0], nums[2])
  return [m, m, m]

#  make ends
def make_ends(nums):
  return [nums[0], nums[-1]]

# make pi
def make_pi():
  return [3, 1, 4]

# rotate left 3
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]] 

# sum 2
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  return nums[0] + nums[1]

# has23
def has23(nums):
  return 2 in nums or 3 in nums

