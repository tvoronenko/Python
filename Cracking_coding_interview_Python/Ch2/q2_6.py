"""
Implement a function to check if a linked list is a palindrome
"""

import random
from LinkedList import LinkedListNode
from LinkedList import randomLinkedList
from LinkedList import  LinkedList
import sys

def reverse_and_clone(node):
    head = None
    while node != None:
        n = LinkedListNode(node.value)
        n.next = head
        head = n
        node = node.next
        
    return head

def is_equal(list_node_1, list_node_2):
    while list_node_1 != None and list_node_2 != None:
        if list_node_1.value != list_node_2.value:
            return False
        list_node_1 = list_node_1.next
        list_node_2 = list_node_2.next
        
    return list_node_1 == None and list_node_2 == None
            
def is_palindrome(node):
    reversed = reverse_and_clone(node)
    return is_equal(node, reversed)

# Iterative approch
def is_palindromeis_iter(node):
    if node == None:
        return None
    fast = node
    slow = node
    firsthalf = []
    while fast != None and fast.next != None:
        firsthalf.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
        slow = slow.next
    while slow != None:
        if firsthalf.pop() != slow.value:
            return False
        else:
            slow = slow.next
    return True

L1 = randomLinkedList(3, 3, 4)
print(L1)
print(is_palindrome(L1.first))

L2 = LinkedList()
for i in range(1,4):
    L2.addNode(i)
for i in range(3, 0, -1):
    L2.addNode(i)
print(L2)
print(is_palindrome(L2.first))
