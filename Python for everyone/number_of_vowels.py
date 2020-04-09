# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:45:16 2019

@author: Dat Nguyen
"""

mystring = input ('Please enter a string: ')
count = 0
for i in range (len(mystring)):
    if mystring[i:i+3] == 'bob':
        count = count +1
print (count)

