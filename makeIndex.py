import sys


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#                                                               #
# CS 352 - Programming Languages                                #
# Programming Project #4 - Python                               #
#                                                               #
# @author:  Mitchell Nguyen                                     #
# @version:  6 December 2017                                    #
#                                                               #
# NOTE: This program additionally performs all 3 enhancements   #
#       that are listed on the assignment description for       #
#       this programming project.                               #
#                                                               #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



################################################################
#
#'createIndex' function:
#       - Should print an index of all words in a single
#         input text-file.
#
# parameter:
#       - fileName
#         (a single string representing the name of given file)
#
################################################################

def createIndex(fileName) :
    
	#open the file 
	f = open(fileName, "r")
	
	#keeps track of what line we are currently reading
	lineCounter = 0
	
	#dictionary that will store keys and values (which are both string-values)
	storedWords = { }

	#read the text in the input-file until we reach the end of the text
	while True:
		#read a single line from the file
		words = f.readline()

		#characters that are not alphabetical-letters should be ignored
		for letter in words:

			#replace all non-[a-zA-Z] characters with whitespaces
			#(for Enhancement #2, ignore single-quote (') characters for now)
			if letter != ' ' and letter.isalpha() == False and letter != '\'':
				words = words.replace(letter, ' ')

		#increment line-counter
		lineCounter += 1             

		#store each word as an element of a whole list, where
		#the separation point of each word is where whitespace occurs
		#between alphabetical characters
		wordList = words.split()

		#keep track of which index a word is located in the newly created list
		idx = 0

		################################################################
		#
		# Enhancement #2 occurs in for-loop below:
		#       - Consider a single-quote to be a part of a word if it
		#         appears in the middle of a word or at the end,
		#         but not at the beginning.
		#       - This will allow contractions and possessives to be
		#         recognized as words.
		#
		################################################################

		#scan through the list of words per line of text in the input-file
		for word in wordList:

			#keep track of if we have found a single-quote character
			#in the word
			foundSingleQuoteChar = False

			#scan through the first half of the word
			for letter in word[0:int(len(word)/2)]:				
				
				#if first half of word has (') single-quote character in it,
				#then indicate that we have found a single=quote character
				if letter == '\'':
					foundSingleQuoteChar = True

			#if a single-quote appears in the beginning of the word,
			#then ignore the single-quote characters
			if foundSingleQuoteChar == True:

				#replace all single-quote characters in the word
				#with an empty-character
				word = word.replace('\'', '')
					
				#reset default for nex word
				foundSingleQuoteChar = False

			#directly re-assign the original word as its modified version
			wordList[idx] = word

			#increment idx-counter to keep track of position of word in list
			#that is currently being looked at
			idx = idx + 1

		################################################################
		#
		# Enhancement #1 occurs in for-loop below:
		#       - Perform case-folding on your comparisons so that,
		#         for example, the words 'Hammer' and 'hammer' are
		#         considered to be he same word.
		#       - Print all words in their lower-case version.
		#
		################################################################
		
		#scan through the list of words per line of text in the input-file
		for word in wordList:
		
			#create a lower-case version of the given word
			lowerCaseWord = word.lower()

			#check to see if the lower-case version of a given word is already in dictionary
			if lowerCaseWord not in storedWords:
				#if key does not already exist in dictionary, then add it
				
				#store word as lower-case version of itself
				storedWords[lowerCaseWord] = str(lineCounter)
			
			else: #if key already exists in dictionary, ...                             
				#if current line-counter does not match with any values
				#of given key, then add the line-counter value as an
				#appendage to the previous line-counter(s)

				#keeps track of if we have found a repeated line-counter value
				lineCounterFoundInKey = False

				#scan through values of each key
				for number in storedWords[lowerCaseWord]:

					#if the given line-number that the word is found on
					#is already a value for the key...
					if str(lineCounter) == number:

						#... then we have found a repeated line-counter value
						lineCounterFoundInKey = True

				#if we have not found a repeated line-counter value...
				if lineCounterFoundInKey == False:

					#... then append new "line-number" to value of given key
					addLineCounter = str(lineCounter)

					#append new "line-number" to existing value in dictionary
					storedWords[lowerCaseWord] = storedWords[lowerCaseWord] + ", " + addLineCounter


				#reset lineCounterInKey back to false for next line's data
				lineCounterFoundInKey == False
		
		#exit loop if no more lines in input-file
		if words == "": break

	#convert keys to list
	resultList = list(storedWords)

	#reorganize and sort elements of list by ASCII value
	resultList.sort()
	
	#print out dictionary that we created by printing out each key
	#and its correlating value
	for word in resultList:
		print(word, storedWords[word])
	
	#close the file
	f.close()


################################################################
#
# Enhancement #3 occurs in the following function:
#
# 'createIndexEnhancment' function:
#       - Should print an index of all words from multiple
#         input files.
#       - Allow multiple files to be indexed by allowing more
#         than one file to be specified in the parameter
#
# parameter:
#       - multipleFileNamesList
#         (a list of file names given by user)
#
################################################################

def createIndexEnhancement(multipleFileNamesList) :

	#open the file 
	firstFile = open(multipleFileNamesList[0], "r")
	
	#keeps track of what line we are currently reading
	lineCounter = 0
	
	#dictionary that will store keys and values (which are both string-values)
	firstStoredWords = { }

	#read the text in the input-file until we reach the end of the text
	while True:
		#read a single line from the file
		words = firstFile.readline()

		#characters that are not alphabetical-letters should be ignored
		for letter in words:

			#replace all non-[a-zA-Z] characters with whitespaces
			#(for Enhancement #2, ignore single-quote (') characters for now)
			if letter != ' ' and letter.isalpha() == False and letter != '\'':
				words = words.replace(letter, ' ')

		#increment line-counter
		lineCounter += 1             

		#store each word as an element of a whole list, where
		#the separation point of each word is where whitespace occurs
		#between alphabetical characters
		wordList = words.split()

		#keep track of which index a word is located in the newly created list
		idx = 0

		################################################################
		#
		# Enhancement #2 occurs in for-loop below:
		#       - Consider a single-quote to be a part of a word if it
		#         appears in the middle of a word or at the end,
		#         but not at the beginning.
		#       - This will allow contractions and possessives to be
		#         recognized as words.
		#
		################################################################

		#scan through the list of words per line of text in the input-file
		for word in wordList:

			#keep track of if we have found a single-quote character
			#in the word
			foundSingleQuoteChar = False

			#scan through the first half of the word
			for letter in word[0:int(len(word)/2)]:				
				
				#if first half of word has (') single-quote character in it,
				#then indicate that we have found a single=quote character
				if letter == '\'':
					foundSingleQuoteChar = True

			#if a single-quote appears in the beginning of the word,
			#then ignore the single-quote characters
			if foundSingleQuoteChar == True:

				#replace all single-quote characters in the word
				#with an empty-character
				word = word.replace('\'', '')
					
				#reset default for nex word
				foundSingleQuoteChar = False

			#directly re-assign the original word as its modified version
			wordList[idx] = word

			#increment idx-counter to keep track of position of word in list
			#that is currently being looked at
			idx = idx + 1

		################################################################
		#
		# Enhancement #1 occurs in for-loop below:
		#       - Perform case-folding on your comparisons so that,
		#         for example, the words 'Hammer' and 'hammer' are
		#         considered to be he same word.
		#       - Print all words in their lower-case version.
		#
		################################################################
		
		#scan through the list of words per line of text in the input-file
		for word in wordList:
		
			#create a lower-case version of the given word
			lowerCaseWord = word.lower()

			#check to see if the lower-case version of a given word is already in dictionary
			if lowerCaseWord not in firstStoredWords:
				#if key does not already exist in dictionary, then add it
				
				#store word as lower-case version of itself
				firstStoredWords[lowerCaseWord] = str(lineCounter)
			
			else: #if key already exists in dictionary, ...                             
				#if current line-counter does not match with any values
				#of given key, then add the line-counter value as an
				#appendage to the previous line-counter(s)

				#keeps track of if we have found a repeated line-counter value
				lineCounterFoundInKey = False

				#scan through values of each key
				for number in firstStoredWords[lowerCaseWord]:

					#if the given line-number that the word is found on
					#is already a value for the key...
					if str(lineCounter) == number:

						#... then we have found a repeated line-counter value
						lineCounterFoundInKey = True

				#if we have not found a repeated line-counter value...
				if lineCounterFoundInKey == False:

					#... then append new "line-number" to value of given key
					addLineCounter = str(lineCounter)

					#append new "line-number" to existing value in dictionary
					firstStoredWords[lowerCaseWord] = firstStoredWords[lowerCaseWord] + ", " + addLineCounter


				#reset lineCounterInKey back to false for next line's data
				lineCounterFoundInKey == False
		
		#exit loop if no more lines in input-file
		if words == "": break

	#convert keys to list
	firstResultList = list(firstStoredWords)

	#append the first file-name to the strings of the values of each key in the current dictionary
	for word in firstResultList:
		firstStoredWords[word] = firstStoredWords[word] + "(" + multipleFileNamesList[0] + ")"

	# go through the rest of the file-names in the given list other than the first file-name
	# by removing the first file-name from the given list of input-files          
	multipleFileNamesList.pop(0)

	#scan through the rest of the input file-names
	for nextFileName in multipleFileNamesList:

		#open the file 
		nextFile = open(nextFileName, "r")
		
		#keeps track of what line we are currently reading
		lineCounter = 0
		
		#dictionary that will store keys and values (which are both string-values)
		nextStoredWords = { }

		#read the text in the input-file until we reach the end of the text
		while True:
			#read a single line from the file
			words = nextFile.readline()

			#characters that are not alphabetical-letters should be ignored
			for letter in words:

				#replace all non-[a-zA-Z] characters with whitespaces
				#(for Enhancement #2, ignore single-quote (') characters for now)
				if letter != ' ' and letter.isalpha() == False and letter != '\'':
					words = words.replace(letter, ' ')

			#increment line-counter
			lineCounter += 1             

			#store each word as an element of a whole list, where
			#the separation point of each word is where whitespace occurs
			#between alphabetical characters
			wordList = words.split()

			#keep track of which index a word is located in the newly created list
			idx = 0

			################################################################
			#
			# Enhancement #2 occurs in for-loop below:
			#       - Consider a single-quote to be a part of a word if it
			#         appears in the middle of a word or at the end,
			#         but not at the beginning.
			#       - This will allow contractions and possessives to be
			#         recognized as words.
			#
			################################################################

			#scan through the list of words per line of text in the input-file
			for word in wordList:

				#keep track of if we have found a single-quote character
				#in the word
				foundSingleQuoteChar = False

				#scan through the first half of the word
				for letter in word[0:int(len(word)/2)]:				
					
					#if first half of word has (') single-quote character in it,
					#then indicate that we have found a single=quote character
					if letter == '\'':
						foundSingleQuoteChar = True

				#if a single-quote appears in the beginning of the word,
				#then ignore the single-quote characters
				if foundSingleQuoteChar == True:

					#replace all single-quote characters in the word
					#with an empty-character
					word = word.replace('\'', '')
						
					#reset default for nex word
					foundSingleQuoteChar = False

				#directly re-assign the original word as its modified version
				wordList[idx] = word

				#increment idx-counter to keep track of position of word in list
				#that is currently being looked at
				idx = idx + 1

			################################################################
			#
			# Enhancement #1 occurs in for-loop below:
			#       - Perform case-folding on your comparisons so that,
			#         for example, the words 'Hammer' and 'hammer' are
			#         considered to be he same word.
			#       - Print all words in their lower-case version.
			#
			################################################################
			
			#scan through the list of words per line of text in the input-file
			for word in wordList:
			
				#create a lower-case version of the given word
				lowerCaseWord = word.lower()

				#check to see if the lower-case version of a given word is already in dictionary
				if lowerCaseWord not in nextStoredWords:
					#if key does not already exist in dictionary, then add it
					
					#store word as lower-case version of itself
					nextStoredWords[lowerCaseWord] = str(lineCounter)
				
				else: #if key already exists in dictionary, ...                             
					#if current line-counter does not match with any values
					#of given key, then add the line-counter value as an
					#appendage to the previous line-counter(s)

					#keeps track of if we have found a repeated line-counter value
					lineCounterFoundInKey = False

					#scan through values of each key
					for number in nextStoredWords[lowerCaseWord]:

						#if the given line-number that the word is found on
						#is already a value for the key...
						if str(lineCounter) == number:

							#... then we have found a repeated line-counter value
							lineCounterFoundInKey = True

					#if we have not found a repeated line-counter value...
					if lineCounterFoundInKey == False:

						#... then append new "line-number" to value of given key
						addLineCounter = str(lineCounter)

						#append new "line-number" to existing value in dictionary
						nextStoredWords[lowerCaseWord] = nextStoredWords[lowerCaseWord] + ", " + addLineCounter


					#reset lineCounterInKey back to false for next line's data
					lineCounterFoundInKey == False
			
			#exit loop if no more lines in input-file
			if words == "": break

		#convert keys to list
		nextResultList = list(nextStoredWords)

		#append the current file-name to the strings of the values of each key in the current dictionary
		for word in nextResultList:
			nextStoredWords[word] = nextStoredWords[word] + "(" + nextFileName + ")"

		#check to see if there are any keys in the current dictionary that are the
		#same keys as the first "master"-dictionary that we created
		#(the "master"-dictionary will hold all the keyd and values for every input file)
		for word in nextResultList :
			
			#if there is a word that doesn't already exist in first "master"-dcitionary,
			#then simply add the given key and its value
			if word not in firstResultList:
				firstStoredWords[word] = nextStoredWords[word]

			#... if word in current dictionary already exists in "master"-dictionary...
			else:

				#... then append the current value to the "master"-dictionary value of correlating key
				firstStoredWords[word] = firstStoredWords[word] + "; " + nextStoredWords[word]

		#close file that we have just read data from
		nextFile.close()

	#close the first input file (that consists of the "master"-dictionary)
	firstFile.close()
    
	#print out the "master"-dictonary by converting the keys of the
	#dictionary to a list
	finalResultList = list(firstStoredWords)

	#reorganize and sort elements of list by ASCII value
	finalResultList.sort()

	#print out "master"-dictionary that we created by printing out
	#each key and its correlating value	
	for word in finalResultList :
		print(word, firstStoredWords[word])


################################################################
#
# 'main' function:
# - prompts user for a file name
# - reads input from user
# - calls createIndex if user gives single file name
# - calls createIndexEnhancement if user gives multiple file names
#
################################################################

#prompt user and read the input line
fileName = input("Please type the name of one or more files. \nIf there is more than one file, \n  please separate each textfile \n  name with a space-character: ")

#determines if user has given more than one file-name into input-line
givenMultipleFileNames = False

for character in fileName:
	#inspect to see if there is white-space in the given filename,
	#which means that the user has given multiple file-names into input-line
	if character == ' ':

		#if there is whitespace in the user-input, then there
		#are multiple file-names that the user has given us
		givenMultipleFileNames = True

#if user has given only one input file-name...
if givenMultipleFileNames == False:
	#call createIndex function (which deals with single file-name input)
	createIndex(fileName)

#if user has given mulltiple input file-names...
else:
	#separate multiple filenames into a list (based on whitespace in user input)
	multipleFileNamesList = fileName.split()

	#call createIndexEnhancement (which deals with more than one file-name inputs)
	createIndexEnhancement(multipleFileNamesList)
	
