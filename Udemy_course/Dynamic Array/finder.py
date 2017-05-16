
# coding: utf-8

# In[25]:

#better result
def finder(arr1,arr2):
    if len(arr1) - len(arr2) != 1:
        return None
    
    count = {}
        
    # Fill dictionary for first string (add counts)
    for number in arr1:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
            
    for number in arr2:
        if number in count:
            count[number] -= 1
        else:
            count[number] = 1
    
    for k in count:
        if count[k] != 0:
            return k

import collections

def finder2(arr1, arr2): 
    
    # Using default dict to avoid key errors
    d=collections.defaultdict(int) 
    
    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1 
    
    # Check if num not in dictionary
    for num in arr1: 
        if d[num]==0: 
            return num 
        
        # Otherwise, subtract a count
        else: d[num]-=1 
        """
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print 'ALL TEST CASES PASSED'

# Run test
t = TestFinder()
t.test(finder)


# In[28]:

arr1 = [1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6,3,7,2,1,4,6,3,7,2,1,4,6,3,7,2,1,4,6,3,7,2,1,4,6,3,7,2,1,4,6]
get_ipython().magic(u'timeit finder(arr1,arr2)')
get_ipython().magic(u'timeit finder2(arr1,arr2)')


# In[8]:

arr1 = [5,5,7,7]
arr2 = [5,7,7]

finder(arr1,arr2)


# In[ ]:



