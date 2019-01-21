# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:54:55 2018

@author: leann
"""

print("Welcome to Glorious Data Bundles 4 you.")

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        print('\nWelcome!\nWhat would you like to do?')
        purchaseType = input('\nPlease select your choice: ')
        
        print('Your balance is', balance, 'GBP')
        print('\nThank you for your custom.')
        return'balance-request'
                
    elif purchaseType == '2':
            return mobileTopUp(balance)
    else:
            print('Error! Transaction type not recongised,\n not a valid option')
            return 'transaction-error'
               
        #else:
        #return 'Oh No! Wrong password, please try again'
        


def passwordCheck_once(truePasscode):
    attempt = input('Please enter your password:  ')
    if attempt == truePasscode:
        return True
    else:
        print('Your paswword is incorrect')
        return False
    
def passwordCheck(truePasscode):
    if passwordCheck_once(truePasscode):
        return True
    print('\nPlease try again(this is your 2nd attempt).')
    if passwordCheck_once(truePasscode):
        return True
    print('\nPlease try again(this is your last attempt).')
    if passwordCheck_once(truePasscode):   
        return True
#return False
        
def checkBalance(balance):
    if balance >0:
        return True
    else:
        print('You require more credit to be added to be in credit with us.')
        return False 

def multipleOfFive(amount):
    return amount ==int(amount / 5.0)*5



def mobileTopUp(balance):
    maxTopUp = 100.00
    print('Please enter the mobile number you wish to top-up: ')
    
    
    number1 = input()
    print('Please RE-ENTER the mobile number again: ')
    number2 = input()
    if number1 == number2:
        print('Max top-up amount is £100.')
        print('Top-up amount must be a multiple of £5')
        amount = float(input('Please enter your top-up amount:'))
        
        if amount > maxTopUp:
            print('Amount exceeds maximum permitted top-up')
            print('Request refused')
            return 'top-up-request:refused'
        elif amount > balance:
            print('Amount exceeds available funds')
            print('Request refused')
            return 'top-up-request:refused'
        
        elif multipleOfFive(amount):
            print('TThank you.\n Your transaction has been authorised.')
            print('Your new account balance is', round(balance - amount, 3),'GBP')
            return 'top-up-request:accepted'
        
        else: 
            print('Your transaction is not valid')
            return 'top-up-request:refused'
    else:
        print('Your numbers do not match. Top up request refused')
        return 'top-up-request:refused'
        