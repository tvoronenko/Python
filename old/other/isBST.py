class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
def isBST(root,max=None,min=None):
    if root==None:
        return True
    if (max!=None and max<root.value) or (min!=None and min>root.value):
        return False
    return isBST(root.left,root.value,min) and  isBST(root.right,max,root.value)
    
a1=Node(1)
b1=Node(3)
c1=Node(6)
a2=Node(2,a1,b1)
b2=Node(7,c1,None)
root=Node(5,a2,b2)
print(isBST(root))
    