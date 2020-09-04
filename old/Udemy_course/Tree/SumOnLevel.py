class TreeNode:
    def __init__(self, value):
        self.value = value
        self.nodes = []
    
        
def sum_on_level(root):
    stack_sum = []
    to_explore = []
    level = 0
    to_explore.append((root,level))

    while to_explore:
        (node,level) = to_explore.pop()
        if len(stack_sum)==level:
            stack_sum.append(0)
        stack_sum[level]+=node.value
        level+=1
        for nxt in node.nodes:
            if nxt is not None:
                to_explore.append((nxt,level))
    print max(stack_sum)

def sum_on_level_recu(root,stack_sum,level=0):
    if root is None:
        return 
    if len(stack_sum)==level:
            stack_sum.append(0)
    stack_sum[level]+=root.value
    level+=1
    for nxt in root.nodes:
           if nxt is not None:
               sum_on_level_recu(nxt,stack_sum,level)

  
root = TreeNode(6)
node1 = TreeNode(4)
node2 = TreeNode(10)
root.nodes = [node1,node2]
node1.nodes = [TreeNode(1),TreeNode(2),TreeNode(3)]
node2.nodes = [TreeNode(5)]
sum_on_level(root)
stack_sum = []
sum_on_level_recu(root,stack_sum)
print stack_sum