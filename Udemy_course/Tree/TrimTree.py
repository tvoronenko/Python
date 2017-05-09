
# coding: utf-8

# In[ ]:

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.right = right
        self.left = left
#post order traversal = > need to start from bottom of tree, from leaves
def trim(current_node,mins,maxs):
    if current_node == None or mins is None or maxs is None:
        raise ValueError("Tree is empty")
    if mins> maxs:
        raise ValueError("Incorrect value")  
    
    if current_node.left!=None:
        current_node.left = trim(current_node.left,mins,maxs)
    if current_node.right!=None:
        current_node.right = trim(current_node.right,mins,maxs)
    
    if mins<=current_node.value<=maxs:
        return current_node
    if current_node.value < mins:
        return current_node.right
    
    if current_node.value > maxs:
        return current_node.left
    

if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(5)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print trim(root,3,5)

