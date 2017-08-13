
# coding: utf-8

# In[31]:

import collections
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 
def levelOrderPrint(tree):
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0
    array_sum = []
    array_sum.append(0)
    level = 0
    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        print currentNode.val,
        array_sum[level] = array_sum[level] + currentNode.val
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount+=1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount+=1
        if currentCount==0:
            #finished printing current level
            print '\n',
            level +=1
            array_sum.append(0)
            currentCount, nextCount = nextCount, currentCount
    print array_sum


# In[32]:

root = Node(1)
n1 = Node(2)
n2 = Node(3)
root.left=n1
root.right = n2
n1.left=Node(4)
n1.right =Node(5)
n2.left=Node(6)
n2.right =Node(7)
levelOrderPrint(root)


# In[ ]:



