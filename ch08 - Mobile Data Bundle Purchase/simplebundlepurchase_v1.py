# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:00:34 2018

@author: leann
"""


print("Welcome to Glorious Data Bundles 4 you.")

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        print('\nWelcome!\nWhat would you like to do?')
        print('\n To see your balance - press 1')
        print('\n To purchase data - press 2')
        decision = input('\nPlease select your choice: ')
               
        if (decision == '1'):
            print ('Your balance is £{}' .format(balance))
            print('\nThank you for your custom.')
            return'balance-request'
        
        elif decision == '2':
            buyingData(balance)

        else:
            print('Your account has currently been locked.\nPlease contact us on 01020 304099')
            return 'transaction-error'

    else:
        return 'Oh No! Wrong password, please try again'
       
  
###entering your password      
def passwordCheck_once(truePasscode):
    attempt = input('Please enter your password:  ')
    if attempt == truePasscode:
        return True
    else:
        print('Your paswword is incorrect')
        return False


####attempts at passwod    
def passwordCheck(truePasscode):
    if passwordCheck_once(truePasscode):
        return True
    print('\nPlease try again(this is your 2nd attempt).')
    if passwordCheck_once(truePasscode):
        return True
    print('\nPlease try again(this is your last attempt).')
    if passwordCheck_once(truePasscode):   
        return True
    
    
##checking balance phone
    
def checkBalance(balance):
    if balance >0:
        return True
    else:
        print('You require more credit to be added to be in credit with us.')
        return False 
    
#buying data
def buyingData(balance):
    gb1= 5
    gb5 = 10
    gb10 = 20
    print('\nWhat would you like to purchase? \nA. 1gb --- £5 \nB. 5g --- £10\nC. 10gb --- £20')
    
    if balance == "A":
        print('You have purchased 1gb.')
        print('Enjoy watching endless videos on cats standing on two legs')
    elif balance == "B":
        print('You have selected 5gb. ')
        print('Enjoy wasting hours of your life online')
    elif balance == "c":
        print('You have selected 10gb. ')
        print('Ever heard of wifi?!')
    else:
        print('That is not an option, please try again')
#        
#####to check mobile number is correct:
#        
def mobileCheck():
    number1 = input('Please enter your mobile number ')
    number2 = input('Please enter your mobile number again ')
    if number1 == number2 :
        return True
    else:
        return False
       
