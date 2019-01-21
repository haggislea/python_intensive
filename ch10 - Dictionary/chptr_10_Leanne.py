# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:37:25 2018

@author: leann
"""

######Salaries######
{'bo':50000, 'linda':30000, 7:('joke','chen','bond')}
#
salary={}

salary

{}
salary['linda'] = 30000
salary
{'linda':30000}

salary['inda'] +=35000

#prints   
salary['linda']
33500

salary['bo'] = +1250
salary['bo']
#prints
1250

#####Telephone directory######

##in class exercise:
tel ={'Kate':949 , 'Pam':579 , 'Me':511}
tel
#Prints
{'Kate': 949, 'Pam': 579, 'Me': 511}

#added anther number
tel['muna'] = 856
tel
#prints
{'Kate': 949, 'Pam': 579, 'Me': 511, 'muna': 856}

tel['Kate'] = 9499

tel
#prints
{'Kate': 9499, 'Pam': 579, 'Me': 511, 'muna': 856}

tel['Pam']=5579

tel
#prints
{'Kate': 9499, 'Pam': 5579, 'Me': 511, 'muna': 856}

tel['Me'] = 2511

tel
#prints
{'Kate': 9499, 'Pam': 5579, 'Me': 2511, 'muna': 856}

tel['muna'] = 8856

tel
#prints
{'Kate': 9499, 'Pam': 5579, 'Me': 2511, 'muna': 8856}

del tel['muna']
tel
#prints   {'Kate': 9499, 'Pam': 5579, 'Me': 2511}

tel.keys() 
#prints
dict_keys(['Kate', 'Pam', 'Me'])


tel.values()
#prints
dict_values([9499, 5579, 2511])


list(tel.keys())[0]
##prints
'Kate'

list(tel.keys())[3]
#prints this error message as there are not 3 items
Traceback (most recent call last):

  File "<ipython-input-80-78d297972390>", line 1, in <module>
    list(tel.keys())[3]

IndexError: list index out of range


list(tel.keys())[0:3]
#prints
['Kate', 'Pam', 'Me']

list(tel.values())[0:3]
##prints out
[9499, 5579, 2511]

--------------------------------------------------------
####out of class work#####

tel = {'mum':1234, 'dad':5678, 'sid':9101112, 'derrick':1234567, 'bunty': 342334}

tel
#prints
{'mum': 1234, 'dad': 5678, 'sid': 9101112, 'derrick': 1234567, 'bunty': 342334}

tel['mum']
#prints
1234



tel['mum'] = 4321

tel
#prints
{'mum': 4321, 'dad': 5678, 'sid': 9101112, 'derrick': 1234567, 'bunty': 342334}

tel.keys()
#prints
dict_keys(['mum', 'dad', 'sid', 'derrick', 'bunty'])



tel.values()
#prints
dict_values([4321, 5678, 9101112, 1234567, 342334])

type(tel.values())
#prints
dict_values

list(tel.keys())[1]
#prints
 'dad'
 
 counts = ['a':3, 'c':1, 'b':5]




tel = {'mum':1234, 'dad':5678, 'sid':9101112, 'derrick':1234567, 'bunty': 342334}

#####
# how to find an error
k = 'eric'
if k in tel:
    print(k, ':', tel[k])
else:
    print(k, 'has not been not found.\nThis person does not seem to exist in our directory,\nplease try again')
    
    


####################my list
#
toys = {'crayons': 4.5, 'playdough': 6, 'firetruck': 7, 'mylittlepony': 8}

funtoys = list(toys.keys())

funtoys
##prints out:
['crayons', 'playdough', 'firetruck', 'mylittlepony']

sorted(toys.items(), key=lambda kv: kv[1], reverse=True)
###prints

[('mylittlepony', 8), ('firetruck', 7), ('playdough', 6), ('crayons', 4.5)]
########
#

######horses list and values and lambda

horse = {'fancy':20, 'deadbeats':100, 'evileyes':4, 'rideslikethewind':70, 'stumpylegs': 300, 'gofasterstripes':1000}
odds_on = list(horse.keys())

odds_on
##prints out names /(keys) only:

['fancy',
 'deadbeats',
 'evileyes',
 'rideslikethewind',
 'stumpylegs',
 'gofasterstripes']

sorted(horse.items(), key=lambda kv: kv[1])
##prints out keys and values:
 
[('evileyes', 4),
 ('fancy', 20),
 ('rideslikethewind', 70),
 ('deadbeats', 100),
 ('stumpylegs', 300),
 ('gofasterstripes', 1000)]

####### osted with kv eauling zero
sorted(horse.items(), key=lambda kv: kv[0])
##prints
[('deadbeats', 100),
 ('evileyes', 4),
 ('fancy', 20),
 ('gofasterstripes', 1000),
 ('rideslikethewind', 70),
 ('stumpylegs', 300)]

####### osted with kv using minus one
sorted(horse.items(), key=lambda kv: kv[-1])
##prints
[('evileyes', 4),
 ('fancy', 20),
 ('rideslikethewind', 70),
 ('deadbeats', 100),
 ('stumpylegs', 300),
 ('gofasterstripes', 1000)]

####print in reverse order
sorted(horse.items(), key=lambda kv: kv[1], reverse=True)
##prints out:
 
[('gofasterstripes', 1000),
 ('stumpylegs', 300),
 ('deadbeats', 100),
 ('rideslikethewind', 70),
 ('fancy', 20),
 ('evileyes', 4)]

####experimented with doing odds on as written as 100/1 (one hundred to one), it divides or gives the number a decimal point, depending on how it is written!

horse = {'fancy':20/1, 'deadbeats':100/2, 'evileyes':4/10, 'rideslikethewind':70/1, 'stumpylegs': 300/1, 'gofasterstripes':1000/1}

odds_on = list(horse.keys())

sorted(horse.items(), key=lambda kv: kv[1])
##prints out:
 
[('evileyes', 0.4),
 ('fancy', 20.0),
 ('deadbeats', 50.0),
 ('rideslikethewind', 70.0),
 ('stumpylegs', 300.0),
 ('gofasterstripes', 1000.0)]

####in class exercise
### metals(keys), density(values), share price(v2), experiment(v3):
    
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals = list(densities.keys())

metals
#prints out
['iron', 'gold', 'zinc', 'lead']

metals.sort(reverse=True, key=lambda m:densities[m])

metals
#prints out
['gold', 'lead', 'iron', 'zinc']



metal = {}
metals ={'iron':[7.8,100,11],'gold':[19.3, 20000, 9], 'zinc':[7.13, 40000,7], 'lead':[11.4, 80, 5]}

precious_metals = list(metals.keys())
precious_metals.sort(reverse=True, key=lambda m:metals[m][1])
precious_metals
##prints
['zinc', 'gold', 'iron', 'lead']

##to print the share price in orer of value
share_price = list(metals.keys())
share_price.sort(key=lambda m:metals[m][0])
share_price
##prints out
['zinc', 'iron', 'lead', 'gold']

experiments = list(metals.keys())
experiments.sort(key=lambda m:metals[m][2])
experiments
#printss out:
['lead', 'zinc', 'gold', 'iron']



#####PHONE BOOK 
phonebook = {}
users = 0
while users < 4:
       print("-" * 50 )
       print('Welcome and Thank you classmate\n for taking part in our survey ')
       classmate1 = input("What's your name? ")
       print('\nA warm welcome {}' .format(classmate1))
       tel_num = input("What is the last 3 digits of your phone number? ")
       lady_luckNum = input("What is your luckiest of ever number? \n You know you have one..... ")
       users_age = int(input("What be your age? "))
       print('Don\'t worry we\'re not using these numbers for our lottery tickets!')
       place_living = input("Whereabouts are you living these days,\njust the name of the place will do.  ")
       postcode = input('\nLast but not least......\n What is the first letter of your postcode?')
       
       #  queens_age = 92
       if users_age == 'users_age' :
           print('You and the Queen are the same age!\n How about that!!')

       users = users + 1
       if users == 4:
           print("Thank you for entering these details.")


       phonebook[classmate1] = (classmate1, tel_num, lady_luckNum, users_age, place_living, postcode)
       print (phonebook)
print (phonebook)
#return phonebook

phonebook = input_phone_book()
print('thank you kindly for taking part')
    
    

####### prints as such ---- version one:

What's your name? 
eddie

What is the last 3 digits of your phone number? 
112

What is your lucky number? If you don't know, take a guess. 
234

How old are you? 
23

What Town/City do you live in? 
tiverton
{'eddie': ('112', '234', 23, 'tiverton')}



#
###### prints as such ---- #######version two:

Welcome and Thank you classmate
 for taking part in our survey 

What's your name? Vesper the Tester

A warm welcome Vesper the Tester

What is the last 3 digits of your phone number? 645

What is your luckiest of ever number? 
 You know you have one..... 2

What be your age? 15
Don't worry we're not using these numbers for our lottery tickets!

Whereabouts are you living these days,
just the name of the place will do.  Scotland


Last but not least......
 What is the first letter of your postcode? E
{'Vesper the Tester': ('Vesper the Tester', '645', '2', 15, 'Scotland', ' E')}
--------------------------------------------------
Welcome and Thank you classmate
 for taking part in our survey 

What's your name? 






























