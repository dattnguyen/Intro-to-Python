# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:26:49 2019

@author: Dat Nguyen
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
mydict = dict ()
mylist = list ()

for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    time = words [5].split (':')
    mydict [time [0]] = mydict.get(time[0],0) +1

for v,k in mydict.items():
    tupple = (v,k)
    mylist.append(tupple)
mylist = sorted (mylist)

for v,k in mylist:
    print (v,k)
    
        
