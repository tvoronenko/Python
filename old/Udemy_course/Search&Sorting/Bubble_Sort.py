
# coding: utf-8

# In[3]:

def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


# In[4]:

arr = [3,2,13,4,6,5,7,8,1,20]
bubble_sort(arr)


# In[5]:

arr


# In[ ]:



