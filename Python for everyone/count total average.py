# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:22:21 2019

@author: Dat Nguyen
"""

total = 0
count = 0
avg = 0
while True:
    numb = input('please enter a number: ')
    if numb == 'done':
        print ('youre done!')
        break
    try:
        numb = float (numb)
    except ValueError:
        print ('please enter a valid number')
        continue     
    total = total + numb
    count = count + 1
    avg = total / count
print ('total is: ', total, ' count is: ', count, ' average is: ', avg)
     