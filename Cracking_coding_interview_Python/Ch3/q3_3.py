'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack 
exceeds some threshold. Implement a data structure "SetOfStacks" that mimics this.
"SetOfStacks" a should be composed of several stacks and should create a new stack 
once the previous one exceeds capacity. "SetOfStacks.push()" and "SetOfStacks.pop()" 
should have behave identically to a single stack (that is pop() should return the 
same values as it would if there were just a single stack).
FOLLOW UP
Implement a function "popAt(int index)" which performs a pop operation on a specific 
substack.
'''
from Other.Data_Structure.Stack import *
class SetOfStacks:
    def __init__(self):
        self.contents = []
        
    def push(self, item):
        try:
            last_stack = self.contents[-1]
        except IndexError:
            # there is nothing in the set of stacks
            last_stack = Stack(5)
            self.contents.append(last_stack)
        
        if len(last_stack.contents) == last_stack.capacity:
            new_stack = Stack(5)
            new_stack.push(item)
            self.contents.append(new_stack)
        else:
            last_stack.push(item)
    
    def pop(self):
        try:
            last_stack = self.contents[-1]
        except IndexError:
            # there is nothing in the set of stacks
            return None
        
        popped = last_stack.pop()
        if len(last_stack.contents) == 0:
            self.contents.pop()
        
        return popped
            
    def __repr__(self):
        return str(self.contents)
