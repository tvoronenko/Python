'''
Given a binary tree, design an algorithm which creates a linked list of all 
the nodes at each depth (e.g. if you have a tree with depth D, you'll have 
D linked lists)
'''
from Other.Data_Structure.Tree import *
from Other.Data_Structure.LinkedList import *
#time O(N)
#space O(log N) recursive calls  - BST
def create_level_linked_list(root, level = 0, lists = []):
    if root == None: #base case
        return
    list_internal = LinkedList()
    if len(lists) == level: #level not contained in list
        #levels are always traversed in order. So, if this is the first time we've
        #visited level i, we must have seen levels 0 through i -1.
        # We can therefore safely add the level at the end
        lists.append(list_internal)
    else:
        list_internal =  lists[level]
    list_internal.addNode(root)
    create_level_linked_list(root.left, level + 1, lists)
    create_level_linked_list(root.right,level + 1, lists)
    return lists 
#TBD
# def create_level_linked_list_interetive(root, level = 0, lists = []):
#     result = []
#     #visit the root
#     current = LinkedList()
#     if (root != None):
#         current.addNode(root)
#     while (current.size > 0 ):
#         result.append(current) #add previous level
#         parents = current #go to next level
#         current = LinkedList()
#         for parent in result[1:]:
#             #visit the children
#             if parent.left != None:
#                 current.addNode(parent.left)
#             if parent.right != None:
#                 current.addNode(parent.right)
#     return result
A = TreeNode(6)
B = TreeNode(4)
C = TreeNode(10)
D = TreeNode(1)
E = TreeNode(2)
F = TreeNode(3)
G = TreeNode(5)

A.left = B
A.right = C

B.left = D
B.right = G
C.right = E
C.left = F
print(A.display_tree())
print(str(create_level_linked_list(A)[2]))
#print(str(create_level_linked_list_interetive(A)[2]))