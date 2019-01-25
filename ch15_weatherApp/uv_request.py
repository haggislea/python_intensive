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


print(uv_indicator)


    
