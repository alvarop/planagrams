#!/usr/bin/python

# Anagram finder!

WORDFILE = '/usr/share/dict/words'

try:
	with open(WORDFILE) as wordList:
		
		# Split into lists of words with the same number of letters
		letterLists = {}
		
		for word in wordList:
			wordLen = len(word.strip())

			if wordLen < 4:
				continue

			if wordLen in letterLists:
				letterLists[wordLen].append(word.strip())
			else:
				letterLists[wordLen] = []
				letterLists[wordLen].append(word.strip())

	# print letterLists
except:
	print('Could not open wordfile \'' + WORDFILE + '\'')

