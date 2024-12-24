class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0

# Example
my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(15)
print("Dequeued Element:", my_queue.dequeue())
