#!/usr/bin/python

# Anagram finder! by Alvaro Prieto
# Change the WORDFILE variable to point to your word file

# Read word file and split into lists of 
# words with the same number of letters
# Also save a sorted version of the word for later use
def getWordLists(wordFilename):
	
	letterLists = {}

	try:
		with open(wordFilename) as wordList:
			for word in wordList:

				word = word.strip() # No newlines please!

				wordLen = len(word)

				# Ignore all the short words
				if wordLen < 4:
					continue

				# Store both the word and a letter-sorted version of it in tuple
				if wordLen in letterLists:
					letterLists[wordLen].append((''.join(sorted(word)), word))
				else:
					letterLists[wordLen] = []
					letterLists[wordLen].append((''.join(sorted(word)), word))
	except:
		print('Could not open wordfile \'' + WORDFILE + '\'')

	return letterLists

# Format list of tuples nicely
def formatWords(wordTupleList):
	words = []
	for wordTuple in wordTupleList:
		words.append(wordTuple[1])

	return ', '.join(words)

# First item in tuple is the letter-sorted word
# if both are the same, they are anagrams!
def isAnagram(wordTuple1, wordTuple2):
	return wordTuple1[0] == wordTuple2[0]

def getAnagrams(wordList):
	# Pre-sort list by sorted letters so we can stop searching
	# for other words as soon as there is a mismatch
	# This should speed things up quite a bit!
	wordList = sorted(wordList, key = lambda x:x[0])

	anagramStrings = []

	while len(wordList) > 0:
		# Remove the first wordTuple. We don't want to match with itself
		currentWordTuple = wordList.pop(0) 

		# Keep track of all matching words here
		currentWords = [currentWordTuple]

		for wordTuple in wordList:
			if(isAnagram(currentWordTuple, wordTuple)):
				currentWords.append(wordTuple)
			else:
				# We can stop searching after the first non-match,
				# since they are all sorted. This makes things fast!
				break

		# Make sure there are at least as many words as there are letters!
		if len(currentWords) >= len(currentWordTuple[1]):
			for index in range(1,len(currentWords)):
				# Remove the used words from the list
				wordList.remove(currentWords[index])
			
			anagramStrings.append(formatWords(currentWords))

	return anagramStrings

#
# Start here!
#
WORDFILE = '/usr/share/dict/words'

wordLists = getWordLists(WORDFILE)

for wordLen in wordLists:
	anagramStrings = getAnagrams(wordLists[wordLen])

	if(len(anagramStrings) > 0):
		print('\n'.join(anagramStrings))
