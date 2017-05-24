'''
Describe how you could use a single array to implement three stacks
'''
#fixed division
class FixedMultiStack:
    def __init__(self,stack_capacity, number_of_stacks = 3):
        self.stack_capacity = stack_capacity
        self.number_of_stacks = number_of_stacks
        self.values = [None] *self.number_of_stacks * self.stack_capacity
        self.sizes = [0] * self.number_of_stacks
        
    #push value onto stack
    def push(self, stack_num, value):
        #check that we have space for the next element
        if(self.is_full(stack_num)):
            raise FullStackException
        #increment stack pointer and then update top value
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value
        
    #pop item from top stack
    def pop(self,stack_num):
        if(self.is_full(stack_num)):
            raise FullStackException
        top_index = self.index_of_top(stack_num) #get top
        value = self.values[top_index] # clear
        self.sizes[stack_num] -= 1 # shrink
        
        return value

    #return top element
    def peek(self, stack_num):
        if(self.is_full(stack_num)):
            raise FullStackException
        return self.values[self.index_of_top(stack_num)]
    
    #return if stack is empty
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    #return if stack is full
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity
    
    #return index of the top of the stack
    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size -1
        
class FullStackException(Exception):
    pass


array = FixedMultiStack(100)
array.push(2, 11)
array.push(2, 13)
print(array.pop(0) ) # Trying to pop an empty stack.
print(array.peek(2)) # 13
array.push(0, 20)
array.push(0, 30)
print(array.pop(0))  # 30
print(array.peek(0)) # 20
    