
"""
Write code to remove duplicates from an unsorted linked list
How would you solve this problem if a temporary buffer is not allowed?
"""
import random
from Other.Data_Structure.LinkedList import *


def delete_duplicates(linked_list_node):
    """
    Using a hash table to keep track of nodes already found
    Time complexity is O(n)
    Space complexity is O(n)
    """
    if not linked_list_node:
        return
    current_node = linked_list_node 
    previous = None
    set_founded = {}
    while current_node != None:
        if current_node.value in set_founded:
            previous.next = current_node.next
        else:
            set_founded[current_node.value] = 1
            previous = current_node
        
        current_node = current_node.next 
    
    return linked_list_node

def delete_dupl_no_buffer(linked_list_node):
    """
    Do this without a buffer (hash table), you will require two "pointers"
    One "pointer" represents the current node being examined
    The other pointer checks all preceding nodes to see if the current node
    has already been encounter
    Space complexity is O(1)
    Time complexity is O(n^2) since you are pretty much comparing every node
    to every other node
    """
    if not linked_list_node:
        return

    current_node = linked_list_node
    while current_node != None:
        #Remove all future node that have the same value
        runner_node = current_node
        while runner_node.next != None:
            if runner_node.next.value == current_node.value:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next

        current_node = current_node.next
     
L1 = randomLinkedList(9, 3, 7)
print(L1)
delete_dupl_no_buffer(L1.first)
print(L1)
        