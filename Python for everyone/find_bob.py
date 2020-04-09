# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:45:57 2019

@author: Dat Nguyen
"""

mystring = input ('please enter a string: ')
mycount = 0
for i in range (len(mystring)):
    if mystring[i:i+3] == 'bob':
        mycount = mycount + 1
print (mycount)

    
    