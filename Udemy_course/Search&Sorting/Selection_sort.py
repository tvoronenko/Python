
# coding: utf-8

# In[28]:

def selection_sort(arr):
    # advance the position through the entire array 
    #   (could do j < n-1 because single element is also min element) 
    n=len(arr)
    for j in range(n): 
        """ find the min element in the unsorted a[j .. n-1] 
        assume the min is the first element """
        i_Min = j
        # test against elements after j to find the smallest
        for i in range(j+1,n):
            # if this element is less, then it is the new minimum
            if (arr[i] < arr[i_Min]):
                # found new minimum; remember its index
                i_Min = i
        if(i_Min != j) :
            arr[j],arr[i_Min]= arr[i_Min], arr[j]


# In[29]:

arr = [3,2,13,4,6,5,7,8,1,20]
selection_sort(arr)


# In[30]:

arr


# In[ ]:



