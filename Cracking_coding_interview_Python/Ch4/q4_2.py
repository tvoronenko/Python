'''
Given a sorted (increasing order) array with unique integer elements, write 
an algorithm to create a binary search tree with minimal height.
'''
from Other.Data_Structure.Tree import *

def create_minimal_BST(array, start, end):
    if start > end :
        return None
    mid = int((start + end) / 2)
    root = TreeNode(array[mid])
    root.left = create_minimal_BST(array, start, mid - 1)
    root.right = create_minimal_BST(array, mid + 1, end)
    return root

intarray1=[1,2,3,4,5,6,7,8,9,10,12]
root = create_minimal_BST(intarray1, 0,len(intarray1)-1)
tree = BinarySearchTree(root)
print(root.display_tree())