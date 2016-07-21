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
    def __init__(self,capacity):
        self.contents = []
        self.capacity = capacity
        
    def push(self, item):
        if (len(self.contents) == 0) or (len(self.contents[-1]) == self.capacity):
            self.contents.append([])  
        self.contents[-1].append(item)  
    
    def pop(self):
        if len(self.contents) == 0:
            return None
        data = self.contents[-1].pop()
        if len(self.contents[-1]) == 0:
            self.contents.pop()
        return data
            
    def __repr__(self):
        return str(self.contents)
    # Pop operation on a specifit sub-stack. (Index begins with 1)
    # Not "rolling over" version. OK with some stacks not at full capacity
    def popAt(self, index):
        if index < 1 or index > len(self.contents) or len(self.contents[index-1]) == 0:
            return None
        else:
            return self.contents[index-1].pop() 

s = SetOfStacks(3)  
l=[1,2,3,4,5,6,7,8]  

for e in l:  
    s.push(e)  
print(s)  
s.popAt(0)  
print(s)  
s.popAt(1)  
print(s)  
s.pop()  
print(s)  
s.pop()  
print(s)  