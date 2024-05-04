class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        newNode = Node(value)
        temp = self.top
        self.top = newNode
        self.top.next = temp
    
    def pop(self):
        if self.top is None:
            return None
        poppy = self.top
        self.top = self.top.next
        return poppy.value
    
    def peek(self):
        return self.top.value
    
    def is_empty(self):
        return self.top == None
    
    def size(self):
        count = 0
        cur = self.top
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def display(self):
        cur = self.top
        while cur:
            print(cur.value, end=" -> ")
            cur = cur.next
        print("None")

    
stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.display()
print(stack.is_empty())
print(stack.size())
print(stack.peek())
stack.display()