'''

@author: solnc
'''
def get_char_number(c):

    a = ord("A")
    z = ord("z")
    val = ord(c)
    if (a <= val) and (val <= z):
        return val - a
    
    return -1

def check_max_one_odd(table_frequency):
    found_odd = False
    for count in table_frequency:
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def is_permutation_of_palindrome(s):
    table_frequency = [s.count(c) for c in s]
    return check_max_one_odd(table_frequency)

  
s="Tact Coa"
print(is_permutation_of_palindrome(s.lower().replace(" ","")))