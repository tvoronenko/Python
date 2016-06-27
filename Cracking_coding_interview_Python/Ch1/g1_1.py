"""
Implement an algorithm to determine if an algorithm contains all unique
characters? What if you cannot use any additional data structures?
- In Java, you can use a boolean array of length 128 (for ascii)
"""

def inUniqueChar(s):
	if s == "":
		return True
	char_set = {}
	for c in s:
		if c in char_set:
			return False
		char_set[c] = 1
	return True
	
def inUniqueCharNoSpace(s):
	"""
    Implementing a solution to this problem without an additional data structure
    requires using bit manipulation
	"""
	checker = 0
	for c in s:
		char_code = ord(c) - ord('a')
		if checker & (1 << char_code):
			return False
		
		checker|=(1 << char_code)
		
	return True
		
if __name__ == '__main__':
	#testing

	#positive test case
	teststringtrue = "abcdefghijkl"
	#negative test case
	teststringfalse = "aabvcgdfgbvxbj"

	#list of all functions to test
	funclist = [inUniqueCharNoSpace,inUniqueChar]

	for func in funclist:
		print("Testing function " + str(func))
		if func(teststringtrue):
			print("Test 1 passed")
		else:
			print("Test 1 failed")
		
		if not func(teststringfalse):
			print("Test 2 passed")
		else:
			print("Test 2 failed")
	