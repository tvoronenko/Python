'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string "aabcccccaaa" would become
"a2b1c5a3". If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume
the string has only upper and lower case letters (a-z)
'''
def compress_string(s):
    result = []
    count = 1
    same_string = True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count +=1
            same_string = False
        else:
            result.append(s[i-1]+str(count))
            count = 1
    result.append(s[-1]+str(count))
    if same_string:
        return s
    else:
        return ''.join(result)

s = 'abcd'
print(compress_string(s))