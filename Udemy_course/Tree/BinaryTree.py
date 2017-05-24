from collections import deque
class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
def inorder_iter(tree):
    done=0
    current = tree
    to_explore = []
    while not done:
        if current is not None:
            to_explore.append(current)
            current = current.getLeftChild()
        else:
            if len(to_explore)>0:
                current = to_explore.pop()
                print current.getRootVal()
                current = current.getRightChild()
            else:
                done=1
        
def preorder_iter(tree):
    to_explore = []
    to_explore.append(tree)
    while to_explore:
        current = to_explore.pop()
        print current.getRootVal()
        if current.getRightChild() is not None:
            to_explore.append(current.getRightChild())
        if current.getLeftChild() is not None:
            to_explore.append(current.getLeftChild())
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postorder_iter(root):
    if root is None:
        return
    to_explore = []
    while True:
        while (root):
            if root.getRightChild() is not None:
               to_explore.append(root.getRightChild())
            to_explore.append(root)
            root = root.getLeftChild()
        root = to_explore.pop() 
        if (root.getRightChild() is not None) and (peek(to_explore)==root.getRightChild()):
            to_explore.pop()
            to_explore.append(root)
            root = root.getRightChild()
        else:
            print root.getRootVal()
            root = None
        if len(to_explore) <=0:
            break
              
def preorder(tree):
    if tree != None:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def level_traverse(tree):
    to_explore = deque()
    to_explore.append(tree)
    while to_explore:
        node = to_explore.popleft()
        print node.getRootVal()
        if node.getLeftChild() is not None:
            to_explore.append(node.getLeftChild())
        if node.getRightChild() is not None:
            to_explore.append(node.getRightChild())
        
r = BinaryTree('5')
r.insertLeft('4')
r.insertRight('6')
r.getRightChild().insertLeft('7')
r.getRightChild().insertRight('8')
r.getLeftChild().insertLeft('2')
r.getLeftChild().insertRight('3')
r.getLeftChild().getLeftChild().insertLeft(1)

level_traverse(r)
print ("!!!")
postorder_iter(r)
# In[ ]:



