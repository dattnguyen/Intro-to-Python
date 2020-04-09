# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:47:02 2019

@author: Dat Nguyen
"""

counts = dict ()
print ('Enter a statement: ')
line = input (' ')
words = line.split()
print ('Words: ', words )
for word in words:
    counts [word] = counts.get(word,0) +1
print ('Counts', counts)
for aaa,bbb in counts.items():
    print (aaa,bbb)
    