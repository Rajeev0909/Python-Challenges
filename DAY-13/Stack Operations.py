class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Stack is empty"
    
    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0

# Example
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print("Top Element:", my_stack.peek())
print("Popped Element:", my_stack.pop())
