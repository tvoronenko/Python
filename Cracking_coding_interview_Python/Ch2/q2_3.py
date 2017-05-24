"""
Implement an algorithm to delete a node in the middle of a singly
linked list, given only access to that node
"""
from Other.Data_Structure.LinkedList import randomLinkedList

def delete_middle(linked_list_node):
    """
    Since you are not given access to the head of the list, you can simply
    copy the data from the next node to the current node and then delete the
    next node.
    This solution does not work if the node to be deleted is the last node.
    """
    if linked_list_node is None or linked_list_node.next is None:
        return
    linked_list_node.value = linked_list_node.next.value
    linked_list_node.next = linked_list_node.next.next
    return True

def main():
    """test"""
    list1 = randomLinkedList(5, 0, 100)
    node = list1.first.next.next# Given access to the 3rd node
    print(list1)
    print("delete: ")
    print(node)
    print("After deleting the node")
    delete_middle(node)
    print(list1)

if __name__ == '__main__':
    main()
