# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:11:47 2019

@author: leann
"""

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('task1.db')

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    

    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")

create_table()
data_entry()

 
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d%H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)', (unix, date, keyword, value))
    conn.commit()
    
for i in range(100):
    dynamic_data_entry()
    time.sleep(1)
    
def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 ')
    for row in c.fetchall():
        print(row)
    conn.commit()
    
def read_from_db2():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix > 1547032329.08789 and unix < 1547032337.73796 ')
for row in c.fetchall():
    print(row[0])    


 
c.close()
conn.close()  