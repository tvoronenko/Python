
# coding: utf-8

# In[46]:

def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum 
#Kadane’s Algorithm:
# Function to find the maximum contiguous subarray
from sys import maxint
def large_cont_sum2(a):
    size = len(a)  
    max_so_far = -maxint - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
         
        if max_ending_here < 0:
            max_ending_here = 0
        
    return max_so_far

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)


# In[47]:

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])


# In[48]:

large_cont_sum2([1,2,-1,3,4,10,10,-10,-1])


# In[ ]:




# In[ ]:



