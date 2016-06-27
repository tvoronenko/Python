'''
Given two strings, write a function to determine if one is a permutation
of the other
Considerations: is comparison case sensitive? Is whitespace significant?
'''
def get_char_number(c):
    """
    Map each character to a number. a ->0, b -> 1, etc
    This is case insensitive. Non-letter character map to -1.
    """
    a = ord('A')
    z = ord('z')
    val = ord(c)
    if ((a<=val) and (val<=z)):
        return val - a
    
    return -1

def build_char__frequency_table(s):
    """
    Count how many times each character appears.
    """
    table = {}
    for c in s:
        x = get_char_number(c)
        if x != -1:
            if x in table:
                table[x]+=1
            else:
                table[x]=1
    return table
       
def check_max_one_odd(table):
    """
    Check that no more than one character has  an odd count
    """ 
    foundOdd = False
    for count in table:
        if (count % 2) == 1:
            if foundOdd:
                return False
            foundOdd = True
    
    return True

def is_permutation_of_palimndrome(s):
    table = build_char__frequency_table(s)
    return check_max_one_odd(table)

def is_permutation_of_palimndrome2(s):
    countOdd = 0
    table = {}
    for c in s:
        x = get_char_number(c)
        if x != -1:
            if x in table:
                table[x]+=1
            else:
                table[x]=1
            if table[x] % 2 == 1:
                countOdd+=1
            else:
                countOdd-=1
    return countOdd <= 1
        
word = "Tact Coa"
print(is_permutation_of_palimndrome2(word.lower()))
    