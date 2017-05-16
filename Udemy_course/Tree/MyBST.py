
# coding: utf-8

# In[ ]:

from collections import deque

class Node:
    def __init__(self, i_data, f_data,  left_child=None, right_child=None, parent=None):
        self.i_data = i_data
        self.f_data = f_data
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent
    
    def display(self):
        print("[{0},{1}]".format(self.i_data, self.f_data))
    
    def is_leaf(self):
        return self.right_child == None and self.left_child == None

class Tree:
    
    def __init__(self, root):
        self.root = root
    #find node interativly
    def find(self, key):
        current = self.root
        while  current.i_data != key and current != None: # find node with given key or didn't find it
            if key < current.i_data: 
                current = current.left_child
            else:
                current = current.right_child
        return current
    
    #find node by recursion
    def find_rec(self, key,current_node):
        if not current_node or key == current_node.i_data: #didn't find it or # find node with given key
            return current_node
        
        if key < current_node.i_data: 
             return self.find_rec(key,current_node.left_child)
        else:
            return self.find_rec(key,current_node.right_child)
           
    def insert(self,key,value):
        new_node =  Node(key,value)
        if not (key or value):
            raise ValueError("Key and/or value is incorrect")
        if not self.root:
            self.root = new_node
            return
        else:
            current = self.root
            while True:
                parent = current
                new_node.parent = parent
                if key < current.i_data:
                    current = current.left_child
                    if not current:
                        parent.left_child = new_node
                        return

                elif current.i_data < key:
                    current = current.right_child
                    if not current:
                        parent.right_child = new_node
                        return
                else:
                    raise ValueError("Such key in tree")
                    
    def insert_rec(self,key,value,current):
        new_node =  Node(key,value)
        if not self.root:
            self.root = new_node
            return
        else:
            if not current:
                return None
            if key < current.i_data:
                if not current.left_child:
                    new_node.parent = current
                    current.left_child = new_node
                else:
                    return self.insert_rec(key,value,current.left_child)
            elif current.i_data < key:
                if not current.right_child:
                    new_node.parent = current
                    current.right_child = new_node
                else:
                    return self.insert_rec(key,value,current.right_child)
            else:
                raise KeyError("Such key in tree")
                
    """ Find minumum from Node current"""
    def find_tree_min(self,current):
        while current.left_child !=None:
            current = current.left_child
        return current
    
    """Delete node with key"""
    def delete(self,key):
        if not key:
            raise ValueError("Key is incorrect")
        del_node = self.find(key)
        if not del_node:
            raise ValueError("Node with such key is not exist")
        if del_node.left_child == None: #node has one right child or none child - replace by its child or none
            self.transplant(del_node,del_node.right_child)
        elif del_node.right_child == None: #node has one left child or none child - replace by its child or none
            self.transplant(del_node,del_node.left_child)
        #node has both child - replace by successor(ith this case min from right child)
        else: #node has both child - replace by successor
            min =  self.find_tree_min(del_node.right_child)
            print min.i_data
            if min !=del_node.right_child:
                self.transplant(min,min.right_child) # place right child of successor instead of successor,
                min.right_child = del_node.right_child
                min.right_child.parent = min
            self.transplant(del_node,min)
            min.left_child = del_node.left_child
            min.left_child.parent = min
        return del_node

    """Transplant nodes""" 
    def transplant(self, to_node, from_node):
        if to_node.parent == None:
            self.root = from_node
        elif to_node == to_node.parent.left_child:
            to_node.parent.left_child = from_node
        else:
            to_node.parent.right_child = from_node
        if from_node != None:
            from_node.parent = to_node.parent
    
    """Find next bigger value after current node"""
    def find_successor(self, current):
        if current.right_child:
            return self.find_tree_min(current.right_child)
        successor = current.parent
        if successor.left == current: 
            return successor
        else:
            return None #no successor
            
        
    def display(self):
        global_stack = deque()
        global_stack.append(self.root)
        n_blanks = 32
        is_row_empty = False
        str_to_print=""
        print ".................................................."
        while (is_row_empty == False):
            local_stack = deque()
            is_row_empty = True
            str_to_print=""
            str_to_print = n_blanks*" "
            while (len(global_stack)!=0):
                temp = global_stack.pop()
                if temp != None :
                    str_to_print = str_to_print + str(temp.i_data)
                    local_stack.append(temp.left_child)
                    local_stack.append(temp.right_child)
                    if temp.left_child != None or temp.right_child != None :
                        is_row_empty = False
                else:
                    str_to_print = str_to_print + "--"
                    local_stack.append(None)
                    local_stack.append(None)
                str_to_print = str_to_print+ ((n_blanks*2) - 2)*" "
            #end while global_stack not empty
            print str_to_print
            print ""
            n_blanks = n_blanks // 2
            while (len(local_stack)!=0) :
                global_stack.append(local_stack.pop())
    
        #end while is_row_empty is false
        print ".................................................."


# In[ ]:

root = Node(4,1)
tree = Tree(root)
tree.insert(2,2)
tree.insert(1,2)
tree.insert(3,4)
root.display()
tree.insert(10,10)
tree.insert(8,10)
tree.insert(9,9)
tree.insert(6,6)
tree.insert(14,6)
tree.insert(12,6)
tree.insert(13,6)
tree.display()
tree.delete(12)
tree.display()