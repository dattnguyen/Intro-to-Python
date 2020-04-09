# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:04:25 2019

@author: Dat Nguyen
"""

#The program works as follows: you (the user) thinks of an integer between 0 
#(inclusive) and 100 (not inclusive). The computer makes guesses, 
#and you give it input - is its guess too high or too low? 
#Using bisection search, the computer will guess the user's secret number!

low = 0
high = 100
ans = int ((low+high)/2.0)
validanswer = ['h','l','c']
print ('Please think of a number between 0 and 100!')
while True:
    print ('Is your secret number ', ans, ' ?')
    uinp = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if uinp not in validanswer :
        print ("You need to enter 'h', 'l', or 'c'.")    
        continue
    if uinp == 'h':
        high = ans
    elif uinp == 'l':
        low = ans
    ans = int((low+high)/2)
    if uinp == 'c':
        print ('Game over. Your secret number was: ', ans)  
        break
    