"""
Write a program to find the node at which the intersection of two singly 
linked lists begins.
For example, the following two linked lists:
A: a1 -> a2 -> c1 -> c2 -> c3
B: b1 -> b2 -> b3 -> c1 -> c2 -> c3
begin to intersect at node c1.
Notes:
* If two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns
* You may assume there are no cycles anywhere in the entire linked structure
"""
from LinkedList import *
class Result:
        def __init__(self, tail, size):
            self.tail = tail
            self.size = size
        
def find_intersection(list1, list2):
    if (list1 == None) or (list2 == None): return 
    
    #Get tail and size
    result1 = get_tail_and_size(list1)
    result2 = get_tail_and_size(list2)
    
    #If different tail nodes, then there's no intersection
    if (result1.tail != result2.tail): return
    
    #set pointers to the start of each linked list
    shorter = list1 if (result1.size < result2. size) else list2
    longer = list2 if (result1.size < result2. size) else list1
    
    #advance the pointer for the longer linked list by difference in lengths
    longer = getKthNode(longer, abs(result1.size - result2.size))
    
    #Move both pointers until you have a collision
    while(shorter != longer):
        shorter = shorter.next
        longer = longer.next
    
    return longer

def get_tail_and_size(list):
    if (list == None): return
    
    size = 1
    current = list
    while (current.next != None):
        size +=1
        current = current.next
        
    return Result(current, size)

def getKthNode(head, k):
    current = head
    while (k > 0 and current != None):
        current = current.next
        k -= 1
    return current
l_inters = LinkedListNode(7)
l_inters.next = LinkedListNode(2)
l_inters.next.next = LinkedListNode(1)

L1 = LinkedList()
L1.addReadyNode(l_inters)
L1.addNode(9)
L1.addNode(5)
L1.addNode(1)
L1.addNode(3)

L2 = LinkedList()
L2.addReadyNode(l_inters)
L2.addNode(6)
L2.addNode(4)



print("First list: " + str(L1))
print("Second list: " + str(L2))

print("Intersection is " + find_intersection(L1.first,L2.first).print_list())
