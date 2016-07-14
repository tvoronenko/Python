'''
     6       6
    / \
   4   10    (14) ← maximum
  /|\   \
 1 2 3   5   11
 
'''
class TreeNode:
    def __init__(self, value):
        self.nodes = []
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Tree:
    def __init__(self, root):
        self.root = root 

def __str__(self):
        node_list = []
        queue = [self.root]
        while queue:
            current_node = queue.pop()
            node_list.append(str(current_node))
            if current_node.left:
                queue.insert(0, current_node.left)
            if current_node.right:
                queue.insert(0, current_node.right)
        
        return ",".join(node_list)
def find_level_sum(tree, sum_list, level):
    if tree == None:
        return
    if len(sum_list) == level:
        sum_list.append(0)
    sum_list[level] = sum_list[level] + tree.value
    for i in range(0, len(tree.nodes)):
        find_level_sum(tree.nodes[i], sum_list, level+1)


def getMax(sum_list):
    max_el = 0
    for i in sum_list:
        if max_el < i:
            max_el = i
    return max_el

A = TreeNode(6)
B = TreeNode(4)
C = TreeNode(10)
D = TreeNode(1)
E = TreeNode(2)
F = TreeNode(3)
G = TreeNode(5)

A.nodes.extend([B,C])

B.nodes.extend([D,E,F,G])
sum_list = []
find_level_sum(A,sum_list,0)
print(getMax(sum_list))


