# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:32:17 2019

@author: Dat Nguyen
"""

import re
fname = input ('enter the name: ')
fh = open (fname)
mysum = 0
mycount = 1
mylist = list ()
for line in fh:
    line = line.rstrip()
    myfind = re.findall('[0-9]+', line)
    if len(myfind) > 0:
        mylist.append(myfind)
        for i in myfind:
            i = float (i)
            mysum = mysum +i
            mycount = mycount +1
print (mylist)
print ('There are: ', mycount, ' numbers in this file')
print ('Total is: ', mysum)
