# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:13:12 2019

@author: leann
"""

import requests

endpoint ="http://api.openweathermap.org/data/2.5/weather"

#------------
# payload are all the variables to make a request to the API to get the data back.  q= query, then grbbing the lcoation and other needed metrics
#
#unicode  special codes
#

payload = {"q" :"Copenhagen, Denmark", "units":"metric", "appid":"API_GOES_HERE"}

response = requests.get(endpoint, params=payload)
data = response.json()

print('\nthis is what data looks like\n\n')
print(data)
#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
#
#print(response.text)
#data = response.json()
#print(response.json)