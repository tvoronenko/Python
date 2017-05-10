
# coding: utf-8

# In[ ]:

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[ ]:

a = Node(1)
b = Node(2)
c = Node(3)


# In[ ]:

a.nextnode = b


# In[ ]:

b.nextnode = c

