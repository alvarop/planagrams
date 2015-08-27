#!/usr/bin/python

# Anagram finder!

WORDFILE = '/usr/share/dict/words'

try:
	with open(WORDFILE) as wordList:
		letterCount = {}
		for word in wordList:
			wordLen = len(word.strip())
			if wordLen in letterCount:
				letterCount[wordLen] += 1
			else:
				letterCount[wordLen] = 1

	print letterCount
except:
	print('Could not open wordfile \'' + WORDFILE + '\'')

