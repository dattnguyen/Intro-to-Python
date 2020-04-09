# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:31:53 2019

@author: Dat Nguyen
"""

secretWord = 'apple' 
lettersGuessed = ['e', 'w', 'k', 'p', 'l', 'e']
def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True              

mylist = list (secretWord)
def getGuessedWord(secretWord, lettersGuessed):
    for i in range (len(mylist)):
        if mylist[i] not in lettersGuessed:
            mylist[i] = '_'
    return "".join (mylist)           
getGuessedWord(secretWord, lettersGuessed)


import string

def getAvailableLetters(lettersGuessed):
    alphabetlist = list (string.ascii_lowercase)
    for i in lettersGuessed:
        if i in alphabetlist:
            alphabetlist.remove(i)
    return "".join(alphabetlist)
getAvailableLetters(lettersGuessed)

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue
        