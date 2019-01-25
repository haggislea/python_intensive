# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:59:29 2019

@author: leann
"""

import requests
import config

endpoint ="http://api.openweathermap.org/data/2.5/uvi/forecast?"

payload ={"lon": 12.56, "lat": 55.67, "cnt": "8", "appid":config.api_key}


response = requests.get(endpoint, params=payload)
data = response.json()

uv_indicator = data[0]['value']
date_and_time = data[0]['date_iso']

#print(uv_indicator)
#print(date_and_time)


print("\nAnd the UV index will be {} on {}.  \n\nThe purpose of this index is to help people protect themselves from UV radiation. " .format(uv_indicator, date_and_time.title()))

     
# PRINTS OUT:


#And the UV index will be 0.38 on 2019-01-26T12:00:00Z.  
#
#The purpose of this index is to help people protect themselves from UV radiation. 
