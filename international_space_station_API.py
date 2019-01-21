# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:32:17 2019

@author: leann
"""


import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

print(data["number"])
print(data)