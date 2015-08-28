#!/usr/bin/python

# Anagram finder!

# Sort the letters in each word
# If the remaining string is the same, then
# we have an anagram!
def isAnagram(word1, word2):
	sortedWord1 = ''.join(sorted(word1))
	sortedWord2 = ''.join(sorted(word2))
	return sortedWord1 == sortedWord2

# Read word file and split into lists of 
# words with the same number of letters
def getWordLists(wordFilename):
	
	letterLists = {}

	try:
		with open(wordFilename) as wordList:
			for word in wordList:
				wordLen = len(word.strip())

				if wordLen < 4:
					continue

				if wordLen in letterLists:
					letterLists[wordLen].append(word.strip())
				else:
					letterLists[wordLen] = []
					letterLists[wordLen].append(word.strip())
	except:
		print('Could not open wordfile \'' + WORDFILE + '\'')

	return letterLists

def getAnagrams(wordList):
	while len(wordList) > 0:
		currentWords = [wordList.pop(0)]

		for word in wordList:
			if(isAnagram(currentWords[0], word)):
				wordList.remove(word)
				currentWords.append(word)

		if len(currentWords) > 3:
			print ', '.join(currentWords)

# Start here
WORDFILE = '/usr/share/dict/words'

wordLists = getWordLists(WORDFILE)

for wordLen in wordLists:
	getAnagrams(wordLists[wordLen])
