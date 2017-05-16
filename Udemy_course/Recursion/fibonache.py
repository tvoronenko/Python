
# coding: utf-8

# In[32]:

def fib_rec(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursion
    else:
        return fib_rec(n-1) + fib_rec(n-2)


# In[33]:

fib_rec(10)


# In[38]:

# Instantiate Cache information

cache = {}

def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        cache[n] =  n
    else:
        if n not in cache:
            # Keep setting cache
            cache[n] =  fib_dyn(n-1)+fib_dyn(n-2)
                
    return cache[n]


# In[39]:

fib_dyn(10)


# In[40]:

def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b
        
    return a


# In[41]:

fib_iter(10)


# In[ ]:

"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print 'Passed all tests.'
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib_rec)
#t.test(fib_dyn) # Note, will need to reset cache size for each test!
#t.test(fib_iter)

