from random import randint

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
    def print_list(self):
        node_str = ""
        current_node = self
        while current_node:
            if current_node.next:
                node_str = node_str + str(current_node.value) + "->"
            else:
                node_str = node_str + str(current_node.value)

            current_node = current_node.next

        return node_str
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0
        
    def addNode(self, value):
        self.size = self.size + 1
        if self.first == None:
            self.first = LinkedListNode(value)
        else:
            oldfirst = self.first
            self.first = LinkedListNode(value)
            self.first.next = oldfirst
    
    def addReadyNode(self, new_node):
        self.size = self.size + 1
        if self.first == None:
            self.first = new_node
        else:
            oldfirst = self.first
            self.first = new_node
            self.first.next = oldfirst
            
            
    def __str__(self):
        if self.first != None:
            index = self.first
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "->".join(nodestore) 
        return ""
    
def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist
