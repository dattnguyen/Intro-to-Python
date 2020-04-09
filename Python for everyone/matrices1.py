# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:43:03 2019

@author: Dat Nguyen
"""


y = float (input ('Please enter a number: '))
epsilon = 0.01
guess = y/2
number = 0
while abs (guess*guess - y) > epsilon:
    number += 1
    guess = guess - (guess*guess-y)/ (2*guess)
print ('The square root of ',y, ' is: ', guess)
print ('It takes ', number, ' guesses to find the answer.')