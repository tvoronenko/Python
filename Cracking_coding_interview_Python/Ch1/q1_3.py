"""
Write a method to replace all spaces in a string with '%20'.
Treat the string as a char array to make it challenging.
Otherwise you would just use string replacement.
Assume the char array has 2 spaces at the end for every one
space in the body, so that you don't have to resize the array.
"""

def replace_space(string, true_length):
    """send to function a list to store each char and change space to '%20',
    then join list into a string"""
    i = true_length - 1
    index = len(string)
    while i >= 0:
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
        i -= 1
    return ''.join(string)

def replace_space1(string):
    """additional space"""
    char_list = []
    string = string.strip()
    for char in string:
        if char == ' ':
            char = '%20'
        char_list.append(char)
    return ''.join(char_list)

def main():
    """test"""
    input_string = "Mr Jonh Smith    "
    converted_lit_from_string = list(input_string)
    expect_output = "Mr%20Jonh%20Smith"
    if replace_space(converted_lit_from_string, 13) == expect_output:
        print("test passed")
    else:
        print("test failed")
        print(replace_space(converted_lit_from_string, 13))
    if replace_space1(input_string) == expect_output:
        print("test passed")
    else:
        print("test failed")
        print(replace_space1(input_string))

if __name__ == '__main__':
    main()
    