
'''
Implement an algorithm to find the kth
 to last element of singly linked list
'''
import random
from Other.Data_Structure.LinkedList import *

def kth_to_last(linked_list_node, k):
    if k < 0:
        return "invalid k"

    p1 = linked_list_node
    p2 = linked_list_node

    for i in range(0, k):
        if p1 == None:
            return "k exceeds the length of linkedlist"
        p1 = p1.next

    while p1 != None:
        p1 = p1.next
        p2 = p2.next

    return p2

L = randomLinkedList(8, 0, 100)
print(L)
print("The 3th to last element is", kth_to_last(L.first, 3))
    