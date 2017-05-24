
'''
Implement an algorithm to find the kth
 to last element of singly linked list
'''
from Other.Data_Structure.LinkedList import randomLinkedList

def kth_to_last(linked_list_node, k):
    "using teo pointers - slow and fsst"
    if k < 0:
        return "invalid k"
    pointer1 = linked_list_node
    pointer2 = linked_list_node
    for i in range(0, k):
        if pointer1 is None:
            return "k exceeds the length of linkedlist"
        pointer1 = pointer1.next
    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer2

def main():
    """test"""
    list1 = randomLinkedList(8, 0, 100)
    print(list1)
    print("The 3th to last element is", kth_to_last(list1.first, 3))

if __name__ == '__main__':
    main()
