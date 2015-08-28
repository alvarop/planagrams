#!/usr/bin/python

# Anagram finder!

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
	while len(wordList) > 0:
		currentWordTuple = wordList.pop(0)
		currentWords = [currentWordTuple]

		for wordTuple in wordList:
			if(isAnagram(currentWordTuple, wordTuple)):
				currentWords.append(wordTuple)

		if len(currentWords) > 3:
			for index in range(1,len(currentWords)):
				# Remove the used words from the list
				wordList.remove(currentWords[index])
			
			printWords(currentWords)

# Start here
WORDFILE = '/usr/share/dict/words'

wordLists = getWordLists(WORDFILE)

for wordLen in wordLists:
	getAnagrams(wordLists[wordLen])
