"""
Given two strings, write a function to determine if one is a permutation
of the other
Considerations: is comparison case sensitive? Is whitespace significant?
"""
# big O complexity depends on python list sort complexity, which should be better than O(n^2)
def permutation(s1, s2):
	if len(s1)!=len(s2):
		return False
		
	return sorted(s1)==sorted(s2)
	
#O(n)
def permutation2(s1,s2):
	if len(s1)!=len(s2):
		return False
	letters = {}	
	for c in s1:
		if c in letters:
			letters[c]=letters[c]+1
		else:
			letters[c]=1
			
	for c in s2:
		if c in letters:
			letters[c]=letters[c]-1
			if letters[c]<0:
				return False
		else:
			return False
	return True
		
def anagram2(s1, s2):
    ''' We just check if the counts of each character are the same '''
    from collections import Counter
    return Counter(s1)==Counter(s2)
	
print(anagram2("dane", "enad"))
print(anagram2("dane", "ead"))
		
