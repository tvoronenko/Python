'''
There are three type of edits that can be performed on string: insert a character, 
remove or replace. Given two string, write function to check if they are one (or zero edits) away

ex:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''

def check_one_away_edit(s_original, s_modifyed):
    if (len(s_original) == len(s_modifyed)):
        #replace a ch
        found_diff = False
        for i in range(0,len(s_original)):
            if(s_original[i] != s_modifyed[i]):
                if (found_diff):
                    return False
                found_diff = True
        return found_diff
    elif(abs(len(s_original)- len(s_modifyed)) == 1):
        #insert or remove a ch
        index1 = 0
        index2 = 0
        if (len(s_original) < len(s_modifyed)):
            s1 = s_original
            s2 = s_modifyed
        else:
            s2 = s_original
            s1 = s_modifyed
        
        found_diff = False
        while (index1 < len(s1) and index2 < len(s2)):
            if(s1[index1] != s2[index2]):
                if (index1!= index2):
                    return False
                found_diff = True
                index2 +=1
            else:
                index2 +=1
                index1 +=1
        return True
    else:
        return False

print(check_one_away_edit("pale", "ple"))
print(check_one_away_edit("pales", "pale"))
print(check_one_away_edit("pale", "bale"))
print(check_one_away_edit("pale", "bae"))

