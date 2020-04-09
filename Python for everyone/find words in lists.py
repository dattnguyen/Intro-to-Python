# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:31:15 2019

@author: Dat Nguyen
"""

fname = input ('Please enter a file name:')
fh = open (fname)
lst = list ()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    lst.append(words[1])
    count = count + 1
for i in lst:
    print (i)
print("There were", count, "lines in the file with From as the first word")