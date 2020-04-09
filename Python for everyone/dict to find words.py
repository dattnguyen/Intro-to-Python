# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:26:18 2019

@author: Dat Nguyen
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mydict = dict ()
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    mydict[words[1]] = mydict.get(words[1],0) + 1

bigword = None
bigcount = None
for aaa,bbb in mydict.items():
    if bigword is None or bbb > bigcount:
       bigword = aaa
       bigcount = bbb
print (bigword,bigcount)

    