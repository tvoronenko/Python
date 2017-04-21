
# coding: utf-8

# In[1]:

class BinHeap:
    #create new empty binary heap
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

#helper method for inserting
    def percUp(self,i):
        
        while i // 2 > 0:
            
            if self.heapList[i] < self.heapList[i // 2]:
                
            
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
#add new item to binary heap
    def insert(self,k):
        
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
#helper method for removing
    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:
            
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
#returns the item with the  minimum key value, leaving the item from heap
    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:
            
            return i * 2
        else:
            
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
# return the item with the minimum key value, removing the item from the heap
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
#build a new heap from a list of keys
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


# In[ ]:



