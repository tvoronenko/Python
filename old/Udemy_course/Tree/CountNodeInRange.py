from MyBST import Node,Tree

def countNode(root, min_v, max_v):
    if root == None:
        return 0
    if min_v==None:
        min_v=float('-inf')
    if max_v==None:
        max_v=float('inf')
    if min_v<=root.i_data<=max_v:
        return 1+countNode(root.left_child,min_v,max_v)+countNode(root.right_child,min_v,max_v)
    if root.i_data < min_v:
        return countNode(root.right_child,min_v,max_v)
    if root.i_data > max_v:
        return countNode(root.left_child,min_v,max_v)
    return 0
    

root = Node(4,1)
tree = Tree(root)
tree.insert(2,2)
tree.insert(1,2)
tree.insert(3,4)
tree.insert(10,10)
tree.insert(8,10)
tree.insert(9,9)
tree.insert(6,6)
tree.insert(14,6)
tree.insert(12,6)
tree.insert(13,6)
tree.display()

print(countNode(root,None,None))
