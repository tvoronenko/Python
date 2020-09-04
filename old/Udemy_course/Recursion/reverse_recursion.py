
# coding: utf-8

# In[4]:

def reverse(s):
    
    #base case
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:])+ s[0]

'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print 'PASSED ALL TEST CASES!'
        
# Run Tests
test = TestReverse()
test.test_rev(reverse)


# In[5]:

reverse('hello world')


# In[ ]:



