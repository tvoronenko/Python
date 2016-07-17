"""
Write a method to replace all spaces in a string with '%20'.
Treat the string as a char array to make it challenging. Otherwise you would just use string replacement.
Assume the char array has 2 spaces at the end for every one space in the body, so that you dont have to resize the array.
"""
# send to function a list to store each char and change space to '%20', then join list into a string
def replaceSpace(string, true_length):
    i = true_length - 1
    index = len(string)
    while i >= 0:
        if string[i] == ' ':
            string[index - 1 ] = '0'
            string[index - 2 ] = '2'
            string[index - 3 ] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
        i -=1
    return ''.join(string)
#additional space
def replaceSpace1(string, true_length):
    charList = []
    string = string.strip()
    for char in string:
        if char == ' ':
            char = '%20'
        charList.append(char)
    return ''.join(charList)

#test
inputStr = "Mr Jonh Smith    "
inputStr = list(inputStr)
expectOutput = "Mr%20Jonh%20Smith"
if replaceSpace(inputStr,13) == expectOutput:
    print("test passed")
else:
    print("test failed")
    print(replaceSpace(inputStr,13))