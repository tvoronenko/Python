'''
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to
check if s2 is
a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle"
is a rotation of "erbottlewat").
'''
def is_substring(string1, string2):
    return string1.find(string2) > -1

def is_rotate(string1, string2):
    """#xy = string1 and yx = string2
    s1s1 = xyxy, so xs2y, so string2 is always substring s1s1"""
    if len(string1) > 0 and len(string1) == len(string2):
        return is_substring(string1*2, string2)
def main():
    """test"""
    string1 = 'waterbottle'
    string2 = 'erbottlewqt'
    print(is_rotate(string1, string2))

if __name__ == '__main__':
    main()
