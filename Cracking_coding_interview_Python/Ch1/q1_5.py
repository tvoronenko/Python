'''
There are three type of edits that can be performed on string: insert a character,
remove or replace. Given two string, write function to check if they are one (or zero edits) away

ex:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''
#more complex but without code repeat
def check_one_away_edit(s_original, s_modifyed):
    #check length
    if abs(len(s_original) - len(s_modifyed)) > 1:
        return False
    #get shorter and longer string
    #shorter
    string1 = s_original if (len(s_original) < len(s_modifyed)) else s_modifyed
    #longer
    string2 = s_modifyed if (len(s_original) < len(s_modifyed)) else s_original
    found_diff = False
    index1 = 0
    index2 = 0
    while index2 < len(string2) and index1 < len(string1):#check boundaries
        if string1[index1] != string2[index2]:
            #ensure that is the first difference found
            if found_diff:
                return False
            found_diff = True
            # on replace, move shorter pointer
            if len(string1) == len(string2):
                index1 += 1
        else:
            index1 += 1

        index2 += 1#always move pointer for longer string
    return True

#more understandable function
def check_one_away_edit1(s_original, s_modifyed):
    found_diff = False
    if len(s_original) == len(s_modifyed):
        #replace a ch
        for i in range(0, len(s_original)):
            if s_original[i] != s_modifyed[i]:
                if found_diff:
                    return False
                found_diff = True
        return found_diff
    elif abs(len(s_original)- len(s_modifyed)) == 1:
        #insert or remove a ch
        index1 = 0
        index2 = 0
        #get shorter and longer string
        #shorter
        string1 = s_original if (len(s_original) < len(s_modifyed)) else s_modifyed
        #longer
        string2 = s_modifyed if (len(s_original) < len(s_modifyed)) else s_original

        while index1 < len(string1) and index2 < len(string2):
            if string1[index1] != string2[index2]:
                if found_diff:
                    return False
                found_diff = True
                index2 += 1
            else:
                index2 += 1
                index1 += 1
        return True
    else:
        return False

def main():
    """test"""
    print(check_one_away_edit1("pale", "ple"))
    print(check_one_away_edit1("pale", "bae"))
    print(check_one_away_edit1("pales", "pale"))
    print(check_one_away_edit1("pale", "bale"))

if __name__ == '__main__':
    main()
