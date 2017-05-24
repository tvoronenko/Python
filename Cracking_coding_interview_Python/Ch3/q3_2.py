'''
How would you design a stack which, in addition to push and pop, has a function min which return the minimum element?
push, pop and min should all operate in O(1) time
'''
from Other.Data_Structure.Stack import *

class StackWithMin(Stack) :
    def push(self, value):
        new_min = min(value,self.min_el())
        return super().push(NodeWithMin(value,new_min))
    
    def min_el(self):
        if (self.isEmpty()):
            return 10000 #error value
        else:
            return self.peek().min_el
    
    def get_min(self):
        if len(self.items) == 0: return None
        return self.items[-1].min_el
    
class NodeWithMin:
    def __init__(self, value, min_el):
        self.value = value
        self.min_el = min_el
        
        


# Testing
from random import randrange
S1 = StackWithMin()
test_list = [randrange(100) for x in range(10)]
for num in test_list:
    S1.push(num)
    print(num)
print("")
for i in range(len(test_list)):
    print("new pop", S1.pop())
    print("new min", S1.get_min())