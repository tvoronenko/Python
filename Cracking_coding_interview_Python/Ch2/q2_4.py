"""
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x
"""
from Other.Data_Structure.LinkedList import LinkedList
#Pass in the head of the linked list and the value to partition around
def partition(linked_list_node, x_value):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    #Partition list
    while linked_list_node != None:
        next_node = linked_list_node.next
        linked_list_node.next = None
        if linked_list_node.value < x_value:
            #insert node into end of before list
            if before_start is None:
                before_start = linked_list_node
                before_end = before_start
            else:
                before_end.next = linked_list_node
                before_end = linked_list_node
        else:
            #insert node in the end after list
            if after_start is None:
                after_start = linked_list_node
                after_end = after_start
            else:
                after_end.next = linked_list_node
                after_end = linked_list_node
        linked_list_node = next_node
    if before_start is None:
        return after_start
    #Merge before list and after list
    before_end.next = after_start
    return before_start

def partition1(linked_list_node, x_value):
    if linked_list_node != None:
        pointer1 = linked_list_node
        pointer2 = linked_list_node.next
        while pointer2 != None:
            if pointer2.value < x_value:
                pointer1.next = pointer2.next
                pointer2.next = linked_list_node
                linked_list_node = pointer2
                pointer2 = pointer1.next
            else:
                pointer1 = pointer1.next
                pointer2 = pointer1.next

def partition2(linked_list_node, x_value):
    head = linked_list_node
    tail = linked_list_node
    while linked_list_node != None:
        next_node = linked_list_node.next
        if linked_list_node.value < x_value:
            linked_list_node.next = head
            head = linked_list_node
        else:
            tail.next = linked_list_node
            tail = linked_list_node
        linked_list_node = next_node
    tail.next = None
    return head

def main():
    """test"""
    list1 = LinkedList()
    list1.addNode(3)
    list1.addNode(5)
    list1.addNode(8)
    list1.addNode(5)
    list1.addNode(10)
    list1.addNode(2)
    list1.addNode(1)
    x_value = 5
    print(list1)
    print(" , x=5")
    partition2(list1.first, x_value)
    print(list1)

if __name__ == '__main__':
    main()
