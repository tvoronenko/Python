"""
Given a circular linked list, implement an algorithm which returns the node
at the beginning of the loop
"""
from Other.Data_Structure.LinkedList import *

def find_begining(head):
    slow = head
    fast = head
    
    #find meeting point. This will be looop_size - k steps into the linked list
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast) : 
            break # collision
        
        #error checking - no meeting point and therefore no loop
    if (fast == None or fast.next == None):
        return None
        
    #move slow to head. Keep fast at meeting point. 
    #each are k steps from the loop start. If they move at same pace,
    #they meet at loop start
    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next
        
    #both now point to the start of loop
    return fast

loop = LinkedListNode("C")
loop.next = LinkedListNode("D")
loop.next.next = LinkedListNode("E")
loop.next.next.next = loop
L1 = LinkedList()
L1.addReadyNode(loop)
L1.addNode("B")
L1.addNode("T")
L1.addNode("R")
L1.addNode("A")

print("start loop is :"+str(find_begining(L1.first)))