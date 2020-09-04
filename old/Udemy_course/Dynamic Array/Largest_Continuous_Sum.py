
# coding: utf-8

# In[19]:

def large_cont_sum2(arr): 
    max_local = arr[0]
    max_global =arr[0]
    for index,i in enumerate(arr,1):
        max_local = max(max_local+i,i)
        max_global = max(max_local,max_global)
    return max_global
#Kadane’s Algorithm:
# Function to find the maximum contiguous subarray
from sys import maxint
def large_cont_sum(a):
    size = len(a)  
    max_so_far = -maxint - 1
    max_ending_here = 0
      
    for i in range(size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
         
        if max_ending_here < 0:
            max_ending_here = 0
        
    return max_so_far


# In[20]:

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])


# In[21]:

large_cont_sum2([-1,-2,-1,-2,-1])


# In[10]:

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


# In[ ]:



