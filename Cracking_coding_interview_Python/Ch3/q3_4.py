'''
Implement a MyQueue class which implements a queue using two stacks.
'''
from Other.Data_Structure.Stack import *
from test.test_xml_etree import ElementSlicingTest

class MyQueue:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()
        
    def size(self):
        return self.stack_newest.size() + self.stack_oldest.size()
    
    def add(self, value):
        #push onto stack_newest which always has newest elements on top
        self.stack_newest.push(value)
        
    #move elements from stack_newest into stack_oldest. This is usually done so that
    #we can do operations on stack_oldest
    def shift_stacks(self):
        if(self.stack_oldest.isEmpty()):
            while(not self.stack_newest.isEmpty()):
                self.stack_oldest.push(self.stack_newest.pop())
                
    def peek(self):
        self.shift_stacks() #ensure stack_oldest has the current elements
        return self.stack_oldest.peek() #retrieve the oldest elements
    
    def remove(self):
        self.shift_stacks()#ensure stack_oldest has the current elements
        return self.stack_oldest.pop()  #pop the oldest elements
    
    def __str__(self):  
        out ="Newer: " + str(self.stack_newest.items ) + " "  + "Older: " + str( self.stack_oldest.items )
        
        return out
    
a = MyQueue()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(str(a))
print(a.remove())
print(str(a))
print(a.peek())
print(str(a))