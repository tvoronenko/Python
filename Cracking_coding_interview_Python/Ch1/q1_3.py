#Write a method to replace all spaces in a string with '%20'.
#Treat the string as a char array to make it challenging. Otherwise you would just use string replacement.
#Assume the char array has 2 spaces at the end for every one space in the body, so that you dont have to resize the array.

def replaceSpaces(s,trueLength):
	spaceCount = 0
	str = None
	for i in range(0,trueLength):
		if s[i] == ' ':
			spaceCount+=1
	
	index = trueLength + spaceCount*2
	if trueLength < len(s):
		s[trueLength] = '\0' #End array
	i = trueLength - 1
	while i>=0:
		if s[i] == ' ':
			s[index - 1] = '0'
			s[index - 2] = '2'
			s[index - 3] = '%'
			index = index - 3
		else:
			s[index-1] = s[i]
			index = index - 1
		i = i -1
		
	return s

inputstring = ["M","R"," ","J","o","h","n"," ","S","m","i","t","h"," "," "," "," "]
	
print(replaceSpaces(inputstring, 13))