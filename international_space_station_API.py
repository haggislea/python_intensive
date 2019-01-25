# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:32:17 2019

@author: leann
"""

#------
# CHECKING TO SEE HOW MANY PEOPLE ARE IN SPACE
#------

import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

number = data['number']
print(number)
