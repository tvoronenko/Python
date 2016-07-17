'''
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to check if s2 is
a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").
'''
def isSubstring(s1,s2):
    return s1.find(s2) > -1
#xy = s1 and yx = s2
# s1s1 = xyxy, so xs2y, so s2 is always substring s1s1
def is_rotate(s1,s2):
    if len(s1) > 0 and len(s1) == len(s2):
        return isSubstring(s1*2,s2)
        
s1 = 'waterbottle'
s2 = 'erbottlewqt'
print(is_rotate(s1,s2))