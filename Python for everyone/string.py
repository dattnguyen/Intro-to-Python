# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:59:30 2019

@author: Dat Nguyen
"""

fname = input ('Please enter the file name: ')
file = open (fname)
count = 0
numb = 0
total = 0
for line in file:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    spam = line.find (':')
    info = line[spam+2:spam+8]
    numb = float (info)
    total = total + numb
    count = count +1    
average = total /count
print ('Average spam confidence: ', average)