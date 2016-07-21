class Stack:
    def __init__(self, capacity = 1000):
        self.items = []
        self.capacity = capacity

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise StackEmptyException
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise StackEmptyException
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
    
class StackEmptyException(Exception):
    pass