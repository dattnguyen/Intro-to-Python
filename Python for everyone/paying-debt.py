# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:20:50 2019

@author: Dat Nguyen
"""

#Write a program to calculate the credit card balance after one year 
#if a person only pays the minimum monthly payment required by 
#the credit card company each month.

balance = float (input ('Please enter your balance: '))
annualInt = float (input ('Please enter your annual interest rate: '))
balance1 = float (balance)
monthlyPay = 10
monthlyInt = annualInt / 12.0
while balance1 >0:
    count = 1
    balance1 = float (balance)
    monthlyInt1 = float (monthlyInt)
    while count < 13:
        balance1 = balance1 - monthlyPay 
        balance1 = balance1 * (1+monthlyInt1)
        count += 1
    monthlyPay += 10
print ('Lowest Payment:', round(monthlyPay-10,2))
