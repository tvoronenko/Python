
# coding: utf-8

# In[164]:

def rearrange(array):
    zero_count = len(array)-1
    for i in range(0,len(array)-1):
        if(i+1 >= zero_count):
            break
        if(array[i] == 0):
            while(array[zero_count] == 0) and zero_count > 0:
                zero_count -= 1
            array[i],array[zero_count] = array[zero_count],array[i]
    return array


# In[165]:

rearrange([0,1,0,2,1])


# In[166]:

rearrange([-1,0,-2,0,1])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



