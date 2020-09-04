'''
Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.
'''
from Other.Data_Structure.Tree import TreeNode
import random

root = TreeNode(random.randint(0,20))
stack = [root]
for i in range(0, 7):
    current_node = stack.pop()
    current_node.left = TreeNode(random.randint(0,20))
    current_node.right = TreeNode(random.randint(0,20))
    stack.insert(0, current_node.left)
    stack.insert(0, current_node.right)
    
        
def check_height(root):
    if root == None:
        return 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1 # not balanced

    right_height = check_height(root.right)
    if right_height == -1:
        return -1 # not balanced

    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return -1
    else:
        return max(left_height, right_height) + 1

def is_balanced(root):
    return check_height(root) != -1

    
print(root.display_tree())
print(is_balanced(root))