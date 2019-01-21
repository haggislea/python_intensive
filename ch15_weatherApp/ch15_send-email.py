# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:43:21 2019

@author: leann
"""
import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd03b17d9b5e349a6a207e02b5e2d17bf.mailgun.org/messages",
        auth=("api", ""),
        data={"from": "Excited User <mailgun@sandboxd03b17d9b5e349a6a207e02b5e2d17bf.mailgun.org>",
              "to": ["fakemynamealways100@geemail.com", "fakemynamealways100@geemail.com@fakkethefakers.com.uk"],
              "subject": "Let's see what'll happen",
              "text": "If it works then we all very lucky!"})
    
send_simple_message()