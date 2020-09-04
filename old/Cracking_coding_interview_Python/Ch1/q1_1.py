"""
Implement an algorithm to determine if an algorithm contains all
unique characters? What if you cannot use any additional data
structures? In Java, you can use a boolean array of length 128
(for ascii)
"""
def unique_characters(my_string):
    """using a hash table (here as a dictionary of key/values)"""
    if my_string == "":
        return True

    character_count = {}
    for character in my_string:
        #checking if char is in the dict is O(1)
        #In practice however, this is expected to perform
        #worse than using lists for small numbers of n.
        if character in character_count:
            return False
        else:
            character_count[character] = True
    return True

def unique_characters_no_ds(my_string):
    """
    Implementing a solution to this problem without an additional data structure
    requires using bit manipulation:
    using a bit vector
    here as assumption in book, assume string only use
    """
    checker = 0
    for character in my_string:
        char_code = ord(character) - ord('A')
        one_left_shift = 1 << char_code
        if checker & one_left_shift > 0:
            return False
        checker = checker | one_left_shift
    return True
def no_duplicates_no_structures(str_):
    """ Now without using additional data structures """

    for letter in str_:
        if str_.count(letter) > 1:
            return False
        else:
            return True

if __name__ == '__main__':
    if unique_characters("dane"):
        print("The characters are unique")
    if not unique_characters("daned"):
        print("The characters are not unique")

    if unique_characters_no_ds("dane"):
        print("The characters are unique")
    if not unique_characters_no_ds("daned"):
        print("The characters are not unique")
