# Programming Assignment No. 02
# Deborah Ruth R. Abad
# 2013-22567
# CMSC 128 AB-7L
# Programming Language : Python

# Getting the Hamming Distance given two strings
# That is the number of inversions per character needed to transfrom string1 to string2 or vise-versa
def getHammingDistance(str1, str2):
	if(type(str1) != str): # checks if the given input is a string
		return "String 1 is not a string."
	if(type(str2) != str): # checks if the given input is a string
		return "String 2 is not a string."
	
	str1 = str1.upper() # to make it case insensitive
	str2 = str2.upper() # to make it case insensitive
		
	if len(str1) != len(str2): # the the 2 strings are not equal in length
		return "Error! Strings are not equal!"
	
	else:
		counter1 = 0
		for letter in range(len(str1)): #since they are of same length
			if(str1[letter] != str2[letter]): # counts number of different letters
				counter1 = counter1 + 1 # counter of different letters
				
		return counter1 # returns the hamming distance
				
# Given a two strings (original and pattern), the function will count the number of occurrence of the pattern in the original.		
def countSubstrPattern(original, pattern): 
	if(type(original) != str): # checks if the input is a string
		return "String 1 is not a string."
	if(type(pattern) != str): # checks if the input is a string
		return "String 2 is not a string."		
	
	original = original.upper() # to make it case insensitive
	pattern = pattern.upper() # to make it case insensitive
	
	counter2 = 0
	
	for sub in range(len(original)):
		if original[sub:sub+len(pattern)] == pattern: # checks if the pattern is a match
			counter2 = counter2 + 1 # if yes, increment the counter
			
	return counter2 # return the number of matches
	
# Returns true if the string is a valid string based on the letters from the given alphabet.
def isValidString(str3, alphabet):
	for found1 in alphabet: # if the letter from str3 is found on the alphabet, then it will be replaced with "*"
		str3 = str3.replace(found1, "*")
	
	for found2 in str3: # if the str3 contains a character which is not *, it will return false
		if found2 != "*":
			isValid = False
			break
		isValid = True # else it will return true

	return isValid
	
# Returns the number of Gs - the number of Cs in the first n...
def getSkew (str4, n1):
	if len(str4) <= 0: # checks if the length is indeed > 0
		return "Invalid input!"
	
	str4 = str4.upper() # to make it case insensitive
	
	countG = 0 # counter for the number of Gs
	countC = 0 # counter for the number of Cs
	 
	for lettergc1 in range(n1): # checks each character of the string
		if str4[lettergc1] == "G": # if the character is G
			countG = countG + 1 # increment counter for G
		if str4[lettergc1] == "C": # if the character is C
			countC = countC + 1 # increment the counter for C
		
	return countG - countC 
	
# Returns the maximum value of the number of skews	
def getMaxSkewN(str5, n2):
	if len(str5) <= 0: # checks if the length is indeed > 0
		return "Invalid input!"
		
	listformax = [] # list for the skews
	
	for lettergc2 in range(1,n2+1): # checks the skew by calling the getSkew(string,int) function : starts with 1 as stated on the specs
		listformax.append(getSkew(str5,lettergc2)) # append the skew on the list
		
	return max(listformax) # returns the maximum
	
# Returns the minimum value of the number of skews	
def getMinSkewN(str6, n3): 
	if len(str6) <= 0: # checks if the length is indeed > 0
		return "Invalid input!" 
		
	listformin = [] # list for the skews
	
	for lettergc3 in range(1,n3+1): # checks the skew by calling the getSkew(string,int) function : starts with 1 as stated on the specs
		listformin.append(getSkew(str6,lettergc3)) # append the skew on the list
		
	return min(listformin)	# returns the minimum	

