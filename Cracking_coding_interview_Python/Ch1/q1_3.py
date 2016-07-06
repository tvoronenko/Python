"""
Write a method to replace all spaces in a string with '%20'.
Treat the string as a char array to make it challenging. Otherwise you would just use string replacement.
Assume the char array has 2 spaces at the end for every one space in the body, so that you dont have to resize the array.
"""# using a list to store each char and change space to '%20', then join list into a string
def replaceSpace(string, true_length):
    newstr = list(string)
    space_count = 0
    for i in range(0,true_length):
        if string[i] == ' ':
            space_count +=1
            
    index = true_length + space_count * 2
    if true_length < len(string):
        newstr[true_length] = '\0' # end array
    i = true_length - 1
    while i >= 0:
        if string[i] == ' ':
            newstr[index - 1 ] = '0'
            newstr[index - 2 ] = '2'
            newstr[index - 3 ] = '%'
            index = index - 3
        else:
            newstr[index - 1] = string[i]
            index -= 1
        i -=1
#     for char in string:
#         if char == ' ':
#             char = '%20'
#         charList.append(char)
#     return ''.join(charList)
    return ''.join(newstr)

def replaceSpace1(string):
    charList = []
    for char in string:
        if char == ' ':
            char = '%20'
        charList.append(char)
    return ''.join(charList)

#test
inputStr = "Mr Jonh Smith     "
expectOutput = "Mr%20Jonh%20Smith"
if replaceSpace(inputStr,13) == expectOutput:
    print("test passed")
else:
    print("test failed")
    print(replaceSpace(inputStr,13))