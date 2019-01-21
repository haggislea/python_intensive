# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:13:12 2019

@author: leann
"""

import requests
import config

endpoint ="http://api.openweathermap.org/data/2.5/weather"

#------------
# payload are all the variables to make a request to the API to get the data back.  q= query, then grbbing the lcoation and other needed metrics
#
#unicode  special codes
#

payload = {"q" :"Copenhagen, Denmark", "units":"metric", "api":"config.api_key"}

response = requests.get(endpoint, params=payload)
data = response.json()

weather = data['weather'][0]['main']
name = data['name']
id = data['main']['temp_min']

print("\n\nThere will be {} in {} and a low of {} today.\n\n Stay safe.".format(weather, name.title(),id))

#-------
# CURRENTLY PRINTING OUT:
#-------

#There will be Snow in Copenhagen and a low of 1 today.
#
# Stay safe.