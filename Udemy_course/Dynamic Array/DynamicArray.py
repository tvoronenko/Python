
# coding: utf-8

# In[13]:

import ctypes

class DynamicArray(object):
    '''Dynamic Array Class (similar to python list)'''
    
    def __init__(self):
        self.n = 0 #count actual elements (default is 0)
        self.capacity = 1 #default capacity
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        """Return number of elements sorted in array"""
        return self.n
    
    def __getitem__(self,k):
        """Return element at index k"""
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!') #check it k index is in bounds of array
        
        return self.A[k]
    
    def append(self,ele):
        """Add element to end of array"""
        if self.n == self.capacity:
            self._resize(2*self.capacity)#Double capacity if not enough room
            
        self.A[self.n] = ele #self.n index to element
        self.n+=1
        
    def _resize(self,new_cap):
        """Resize internal array to capacity new_cap"""
        
        B = self.make_array(new_cap) #new bigger array
        
        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B #Call the new bigger array
        self.capacity = new_cap #Reset the capacity
        
    def make_array(self, new_cap):
        """Return a new array with new_capacity"""
        return (new_cap * ctypes.py_object)()


# In[14]:

#Instantiate
arr = DynamicArray()


# In[15]:

#Append new element
arr.append(1)


# In[16]:

#Check length
len(arr)


# In[17]:

arr.append(2)


# In[18]:

len(arr)


# In[19]:

arr[0]


# In[20]:

arr[1]


# In[ ]:



