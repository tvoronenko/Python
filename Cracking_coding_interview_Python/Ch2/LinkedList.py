from random import randint

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
        
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
            
    def __str__(self):
        if self.first != None:
            index = self.first
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"
    
def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist
