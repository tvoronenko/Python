
# coding: utf-8

# In[58]:

def compress2(s):
    i = 0
    result = []
    count = 0
    
    l = len(s)
    
     # Check for length 0
    if l == 0:
        return ""
    
      # Check for length 1
    if l == 1:
        return s + "1"
    
    for i in range(l-1):
        count += 1
        if s[i] != s[i+1]:
            result.append(s[i]+str(count))
            count = 0
    result.append(s[i]+str(count+1))
    return "".join(result)

def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    
    return r

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestCompress()
t.test(compress)


# In[59]:

get_ipython().magic(u"timeit compress2('AAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCC')")


# In[60]:

get_ipython().magic(u"timeit compress('AAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCCAAAAABBBBCCCC')")


# In[ ]:



