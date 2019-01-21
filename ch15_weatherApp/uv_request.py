# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:59:29 2019

@author: leann
"""

import requests

endpoint ="http://api.openweathermap.org/data/2.5/uvi?appid={appid}&lat={lat}&lon={lon}"

payload ={"lon": 12.57, "lat": 55.69, "cnt": "8", "appid":"5a83590ea2392078ba2a53e072fed9e0"}


response = requests.get(endpoint, params=payload)
data = response.json()

#print("\n {}'s weather is .")
print(data)