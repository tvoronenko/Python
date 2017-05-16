
# coding: utf-8

# In[111]:

def rec_coin(target,coins,known_results):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)
    
    OUTPUT: Minimum number of coins needed to make the target.
    '''
    
    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
     # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
         for i in [c for c in coins if c <= target]:
            num = 1 + rec_coin((target - i),coins,known_results)
            if num < min_coins:
                min_coins = num
                # Reset the known result
                known_results[target] = min_coins
            
    return min_coins



# In[112]:

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

rec_coin(target,coins,known_results)


# In[113]:

"""
RUN THIS CELL TO TEST YOUR FUNCTION.
NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION 
      GO CHECK THE SOLUTION NOTEBOOK INSTEAD OF RUNNING THIS!
"""

from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        print 'Passed all tests.'
# Run Test

test = TestCoins()
test.check(rec_coin)


# In[ ]:




# In[ ]:



