
# coding: utf-8

# In[71]:

#dynamic programming
def max_sub_array(nums):
    #for storing bigger sum for i  between max(i,sum(i-1)+i)
    additional_sum = nums[0] + nums[1]
    #select max for i between maxim(i-1) and sum(i)
    maxim = nums[0] + nums[1]
    for i in range(2,len(nums)):
        additional_sum = max(nums[i]+nums[i-1],nums[i]+additional_sum)            
        maxim = max(additional_sum,maxim)
    return maxim


# In[72]:

max_sub_array([-2,-1,-3,-4,-1])


# In[73]:

max_sub_array([10,-2,3,-7,8,-4,-2,5])


# In[ ]:



