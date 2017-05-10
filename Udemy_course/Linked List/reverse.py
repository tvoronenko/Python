
# coding: utf-8

# In[103]:

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# In[104]:

def reverse(head):
    
    stack = []
    len = 0
    while head.nextnode:
        stack.append(head)
        head = head.nextnode
        len +=1
        
    while len > 0:
        head.nextnode = stack.pop()
        head = head.nextnode
        len -= 1
        
    return head

def reverse2(head):
    
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous


# In[105]:

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


# In[106]:

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value


# In[107]:

d.nextnode.value


# In[108]:

reverse2(a)


# In[109]:

print d.nextnode.value
print c.nextnode.value
print b.nextnode.value


# In[ ]:




# In[ ]:




# In[ ]:



