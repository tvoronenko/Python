'''
Write a program to sort a stack in ascending order (with biggest items on top). 
You may use at most one additional stack to hold items, but you may not copy 
the elements into any other data structure (such as an array). The stack 
supports the following operations: push, pop, peek and isEmpty
'''
from Other.Data_Structure.Stack import *
#space O(n)
#time O(n^2)
class StackWithSort(Stack):
    def sort(self):
        r = Stack()
        while(not self.isEmpty()):
            #insert each element in s in sorted order into r
            tmp = self.pop()
            while ( not r.isEmpty() and r.peek() > tmp):
                self.push(r.pop())
            r.push(tmp)
        
        #copy the elements from r back into s
        while( not r.isEmpty()):
            self.push(r.pop())


s = StackWithSort()  
l=[3,2,4,1,2]  
for e in l:  
    s.push(e) 
print(str(s)) 
s.sort()
print(str(s)) 