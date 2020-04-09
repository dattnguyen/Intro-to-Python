# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:26:01 2019

@author: Dat Nguyen
"""
#Write a program that prints the longest substring of s 
#in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh

def isalphabet(word):
    return word == ''.join(sorted(word))

mystring = input ('please enter a string: ')
mylist = list ()
mycount = 0
myword = 0
for i in range (len(mystring)):
    for a in range (len (mystring)):
        if isalphabet (mystring[i:i+a]) == True:
            mylist.append(mystring[i:i+a])
for i in range (len (mylist)):
    if len(mylist[i]) > mycount:
        mycount = len(mylist[i])
        myword = mylist[i]
print ('Longest word is: ', myword, 'with ', mycount, ' characters')

        


    