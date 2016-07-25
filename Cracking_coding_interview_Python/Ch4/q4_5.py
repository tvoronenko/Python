'''
implement a function if a binary tree is a binary search tree
'''
from Other.Data_Structure.Tree import *

#in-order traversal
#we assume that the tree does't have duplicate

last_printed = None
def checkBST1(root):
    global last_printed
    if root == None: return True
    #check/ recurse left
    if not checkBST1(root.left): return False
    #check current
    if last_printed != None and root.value <= last_printed:
        return False
    last_printed = root.value
    #check / recurse right
    if not checkBST1(root.right): return False
    return True #all good

def valid_bsearch_tree2(root):
    #in-order method
    l = in_order_search(root)
    if sorted(l) == l:
        return True
    return False

def in_order_search(root):
    if root is None: return []
    return in_order_search(root.left) + [root.value] + in_order_search(root.right)
#All the left children of a node can have a MAX value of the parent node
#All the right children of a node can have a MIN value of the parent node
def valid_bsearch_tree(root, lbound = -float("inf"), rbound = float("inf")):
    if root is None: return True
    return (lbound <= root.value < rbound) and \
        valid_bsearch_tree(root.left, lbound, root.value) and \
        valid_bsearch_tree(root.right, root.value, rbound)
#time O(N)
#space O(log N)        
def checkBST2(root,mini = None,maxi = None):
    if root == None:
        return True
    elif (mini != None and root.value <= mini) or (maxi != None and root.value > maxi):
        return False
    elif checkBST2(root.left, mini, root.value) == False or checkBST2(root.right, root.value, maxi) == False:
        return False
    return True        
#valid BST
root = TreeNode(20)
bintree = BinarySearchTree(root)
bintree.insert(10)
bintree.insert(30)
bintree.insert(5)
bintree.insert(15)
bintree.insert(3)
bintree.insert(7)
bintree.insert(17)    

print(checkBST1(root)) 
print(checkBST2(root)) 
print(valid_bsearch_tree2(root)) 
print(valid_bsearch_tree(root)) 
#invalid BST
root = TreeNode(20)
root.left = TreeNode(500)
bintree = BinarySearchTree(root)
bintree.insert(10)
bintree.insert(30)
bintree.insert(5)
bintree.insert(15)
bintree.insert(3)
bintree.insert(7)
bintree.insert(17)

print(checkBST1(root)) 
print(checkBST2(root)) 
print(valid_bsearch_tree2(root)) 
print(valid_bsearch_tree(root)) 
      
