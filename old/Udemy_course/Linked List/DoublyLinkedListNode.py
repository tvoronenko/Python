
# coding: utf-8

# In[ ]:

class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.next_node = None
        self.prev_node = None


# In[ ]:

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)


# In[ ]:

# Setting b after a
b.prev_node = a
a.next_node = b


# In[ ]:

# Setting c after a
b.next_node = c
c.prev_node = b

