
# coding: utf-8

# In[9]:

def insertion_sort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


# In[10]:

arr =[3,5,4,6,8,1,2,12,41,25]
insertion_sort(arr)
arr


# In[ ]:




# In[ ]:



