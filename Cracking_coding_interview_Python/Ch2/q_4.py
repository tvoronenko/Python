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
            #insert node in the end 
                

#----------------test-----------------
L = randomLinkedList(10, 0, 50)
x = 25

print(L)
print(" , x=25")   
partition(L, x)
print(L) 