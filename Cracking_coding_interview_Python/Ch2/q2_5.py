from Other.Data_Structure.LinkedList import LinkedList
from Other.Data_Structure.LinkedList import LinkedListNode
"""
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.
ex: input (7->1->6) + (5->9->2) 617+295
output (2->1->9) 912

Suppose the digits are stored in forward order. Repeat the above problem.
ex: input (6->1->7)+ (2->9->5) 617+295
output (9->1->2"""

def linked_list_add(first_linked_list, second_linked_list, carry):
    """
    The numbers are stored in reverse order
    """
    if not first_linked_list and not second_linked_list and carry == 0:
        return None
    value = carry
    if first_linked_list:
        value = value + first_linked_list.value
    if second_linked_list:
        value = value + second_linked_list.value
    result = value % 10# the last digit
    result_linked_list = LinkedListNode(result)
    #recurse
    if first_linked_list or second_linked_list:
        next_node = linked_list_add(None if not first_linked_list else first_linked_list.next,
                                    None if not second_linked_list else second_linked_list.next,
                                    0 if value < 10 else 1)
        result_linked_list.next = next_node
    return result_linked_list

def linked_list_add_forward(list1, list2):
    # compare length of linked lists and pad the shorter one with 0
    l1_len = len_list(list1)
    l2_len = len_list(list2)
    if l1_len < l2_len:
        list1 = pad_in_front(list1, l2_len - l1_len)
    else:
        list2 = pad_in_front(list2, l1_len - l2_len)
    # Add lists
    sumandcarry = add_lists_fwd_2_helper(list1, list2)
    #If there was a carry value left over, insert this at the front of the lit
    #Otherwise, just return the linked list
    result = LinkedList()
    result.first = sumandcarry[0]
    # If the carry is not 0, insert this at the front of the linked list
    if sumandcarry[1] == 0:
        return result
    else:
        result = insert_before(result, sumandcarry[1])
        return result

# Helper function for recursive adding lists
def add_lists_fwd_2_helper(pointer1, pointer2):
    if (pointer1 is None) and (pointer2 is None):
        sumandcarry = [None, 0]# a python list stores sum node and carry
        return sumandcarry
    #Add smaller digit recursively
    sumandcarry = add_lists_fwd_2_helper(pointer1.next, pointer2.next)
    #Add carry to current data
    val = pointer1.value + pointer2.value + sumandcarry[1]
    #Insert sum of current digits
    dig_node = insert_before(sumandcarry[0], val%10)
    carry = int(val/10)
    return [dig_node, carry]

# Helper function to insert node before a node
def insert_before(node, value):
    new_node = LinkedListNode(value)
    if node != None:
        new_node.next = node
    return new_node

# Helper function to pad the list with zeros in front
def pad_in_front(linkedlist, padding):
    head = linkedlist
    for i in range(padding):
        insert_before(head, 0)
    return head

# Helper function to calculate length of a linked list
def len_list(linkedlist):
    length = 0
    current = linkedlist
    while current != None:
        length += 1
        current = current.next
    return length

def main():
    """test"""
    first_number = LinkedList()
    first_number.addNode(6)
    first_number.addNode(1)
    first_number.addNode(7)

    second_number = LinkedList()
    second_number.addNode(2)
    second_number.addNode(9)
    second_number.addNode(5)

    print("First number: " + str(first_number))
    print("           +    ")
    print("Second number: " + str(second_number))
    print("           =    ")
    print(linked_list_add(first_number.first, second_number.first, 0).print_list())
    print("===================================================")

    first_number = LinkedList()
    first_number.addNode(7)
    first_number.addNode(1)
    first_number.addNode(6)

    second_number = LinkedList()
    second_number.addNode(5)
    second_number.addNode(9)
    second_number.addNode(2)

    print("First number: " + str(first_number))
    print("           +    ")
    print("Second number: " + str(second_number))
    print("           =    ")
    print(str(linked_list_add_forward(first_number.first, second_number.first)))
    print("===================================================")

if __name__ == '__main__':
    main()
