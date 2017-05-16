
# coding: utf-8

# In[8]:

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.right = right
        self.left = left

def isBST(current_node,mins,maxs):
    if current_node == None:
        return True
    if (mins!=None and mins>=current_node.value) or (maxs!=None and maxs<current_node.value):
        return False
    return isBST(current_node.left,mins,current_node.value) and isBST(current_node.right,current_node.value,maxs)

     


# In[10]:

if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(5)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print _isBST(root,None,None)


# In[ ]:




# In[ ]:



