#!/usr/bin/python

# Anagram finder! by Alvaro Prieto
# Change the WORDFILE variable to point to your word file

# Sort the letters in each word
# If the remaining string is the same, then
# we have an anagram!
def isAnagram(wordTuple1, wordTuple2):
	return wordTuple1[0] == wordTuple2[0]

# Read word file and split into lists of 
# words with the same number of letters
# Also save a sorted version of the word for later use
def getWordLists(wordFilename):
	
	letterLists = {}

	try:
		with open(wordFilename) as wordList:
			for word in wordList:

				word = word.strip()

				wordLen = len(word)

				if wordLen < 4:
					continue

				if wordLen in letterLists:
					letterLists[wordLen].append((''.join(sorted(word)), word))
				else:
					letterLists[wordLen] = []
					letterLists[wordLen].append((''.join(sorted(word)), word))
	except:
		print('Could not open wordfile \'' + WORDFILE + '\'')

	return letterLists

def printWords(wordTupleList):
	words = []
	for wordTuple in wordTupleList:
		words.append(wordTuple[1])

	print ', '.join(words)

def getAnagrams(wordList):
	# Pre-sort list by sorted letters so we can stop searching
	# for other words as soon as there is a mismatch
	# This should speed things up quite a bit!
	wordList = sorted(wordList, key = lambda x:x[0])

	while len(wordList) > 0:
		currentWordTuple = wordList.pop(0)
		currentWords = [currentWordTuple]

		for wordTuple in wordList:
			if(isAnagram(currentWordTuple, wordTuple)):
				currentWords.append(wordTuple)
			else:
				# We can stop searching after the first non-match,
				# since they are all sorted
				break

		# Make sure there are at least as many words as there are letters!
		if len(currentWords) >= len(currentWordTuple[1]):
			for index in range(1,len(currentWords)):
				# Remove the used words from the list
				wordList.remove(currentWords[index])
			
			printWords(currentWords)

#
# Start here!
#
WORDFILE = '/usr/share/dict/words'

wordLists = getWordLists(WORDFILE)

for wordLen in wordLists:
	getAnagrams(wordLists[wordLen])
