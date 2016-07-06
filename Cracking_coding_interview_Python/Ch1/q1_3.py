"""
Write a method to replace all spaces in a string with '%20'.
Treat the string as a char array to make it challenging. Otherwise you would just use string replacement.
Assume the char array has 2 spaces at the end for every one space in the body, so that you dont have to resize the array.
"""# using a list to store each char and change space to '%20', then join list into a string
def replaceSpace(string):
    charList = []
    for char in string:
        if char == ' ':
            char = '%20'
        charList.append(char)
    return ''.join(charList)

#test
inputStr = " Smith    q m "
expectOutput = "%20Smith%20%20%20%20q%20m%20"
if replaceSpace(inputStr) == expectOutput:
    print("test passed")
else:
    print("test failed")