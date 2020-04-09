# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:44:56 2019

@author: Dat Nguyen
"""
smallest = None
highest = None

while True:
    numb = input('please enter a number: ')
    if numb == 'done':
        break
    try:
        numb = float (numb)
    except:
        print ('Invalid input')
        continue     
    if highest is None:
        highest = numb
    elif numb > highest:
        highest = numb
    if smallest is None:
        smallest = numb
    elif numb < smallest:
        smallest = numb
print ('Maximum is ', highest)
print ('Minimum is: ', smallest)
 