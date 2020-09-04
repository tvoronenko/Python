'''
write an algorithm to fint the  'next' node (i.e., in-order successor) of a given node in a binary search btre.
You may assume that each node has a link to its parent.
'''
from Other.Data_Structure.Tree import *

def left_most_child(node):
    if node == None:
        return None
    while node.left != None:
        node = node.left
    return node

def in_order_succ(root):
    if root == None:
        return None
    #found right children -> return leftmost node of right subtree
    if root.left != None:
        return left_most_child(root.right)
    else:
        q = root
        x = q.parent
        #go up until we are on left instead of right 
        while(x != None and x.left != q):
            q = x
            x = x.parent
        return x
from random import randrange
def make_random_bsearch_tree(depth = 2, l = -10, r = 20, parent = None):
    if depth < 0 or l == r: return None
    tree = TreeNode(randrange(l, r))
    tree.parent = parent
    tree.left = make_random_bsearch_tree(depth - 1, l, tree.value, tree)
    tree.right = make_random_bsearch_tree(depth - 1, tree.value, r, tree)
    return tree

root = make_random_bsearch_tree()  
print(root.display_tree())
print(in_order_succ(root.left))