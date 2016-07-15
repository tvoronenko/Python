'''
Given a string, write a fucntion to check if it is a permutation of palindrome. A palindrome is a word or phrase
that is the same forwards and backwards. A permutatuion is rearrangement of letters. The palindrome does not
 need to be limited to just dictionary words
'''

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