
# coding: utf-8

# In[24]:

def uni_char(s):
    if len(s) == 0 or len(s) == 1:
        return True
    
    dict_list = []
    for sym in s:
        if sym in dict_list:
            return False
        else:
            dict_list.append(sym)
    return True

def uni_char2(s):
    return len(set(s)) == len(s)

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)


# In[25]:

get_ipython().magic(u"timeit uni_char('abcdefg')")


# In[23]:

get_ipython().magic(u"timeit uni_char2('abcdefg')")


# In[ ]:



