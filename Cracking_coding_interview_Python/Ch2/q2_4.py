"""
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x
"""
import random
from LinkedList import *
#Pass in the head of the linked list and the value to partition around
def partition(linked_list_node, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    
    #Partition list
    while linked_list_node != None:
        next = linked_list_node.next
        linked_list_node.next = None
        if linked_list_node.value < x:
            #insert node into end of before list
            if before_start == None:
                before_start = linked_list_node
                before_end = before_start
            else:
                before_end.next = linked_list_node
                before_end = linked_list_node
        else:
            #insert node in the end after list
            if after_start == None:
                after_start = linked_list_node
                after_end = after_start
            else:
                after_end.next = linked_list_node
                after_end = linked_list_node
        linked_list_node = next
    if before_start == None:
        return after_start
        
    #Merge before list and after list
    before_end.next = after_start
    return before_start
            
def partition1(linked_list_node, x):
    if linked_list_node != None:
        p1 = linked_list_node
        p2 = linked_list_node.next
        while p2 != None:
            if p2.value < x:
                p1.next = p2.next
                p2.next = linked_list_node
                linked_list_node = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next                

def partition2(linked_list_node, x):
    head = linked_list_node
    tail = linked_list_node
    while linked_list_node != None:
        next = linked_list_node.next
        if linked_list_node.value < x:
            linked_list_node.next = head
            head = linked_list_node
        else:
            tail.next = linked_list_node
            tail = linked_list_node
        linked_list_node = next
    tail.next = None
    
    return head
        
#----------------test-----------------
L = LinkedList()
L.addNode(3)
L.addNode(5)
L.addNode(8)
L.addNode(5)
L.addNode(10)
L.addNode(2)
L.addNode(1)
x = 5

print(L)
print(" , x=5")   
partition2(L.first, x)
print(L) 