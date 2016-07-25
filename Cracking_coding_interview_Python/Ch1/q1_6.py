'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string "aabcccccaaa" would become
"a2b1c5a3". If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume
the string has only upper and lower case letters (a-z)
'''
def compress_string(string):
    result = []
    count = 1
    same_string = True
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
            same_string = False
        else:
            result.append(string[i-1]+str(count))
            count = 1
    result.append(string[-1]+str(count))
    if same_string:
        return string
    else:
        return ''.join(result)

def main():
    """test"""
    string = 'abcd'
    print(compress_string(string))

if __name__ == '__main__':
    main()
