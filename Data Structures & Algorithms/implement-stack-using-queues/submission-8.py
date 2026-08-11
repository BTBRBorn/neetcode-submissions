class ListNode:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val):
        new_node = ListNode(val)
        if self.isEmpty():
            self.head = new_node
        elif self.get_length() == 1:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return None
        val = self.head.val
        if self.get_length() == 1:
            self.head = None
        elif self.get_length() == 2:
            self.head = self.head.next
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return val

    def get_length(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.temp = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        
    def pop(self) -> int:
        if self.queue.isEmpty():
            return -1
        while self.queue.get_length() != 1:
            self.temp.enqueue(self.queue.dequeue())
        top_val = self.queue.dequeue()
        self.queue = self.temp
        self.temp = Queue()
        return top_val

    def top(self) -> int:
        if self.queue.isEmpty():
            return -1
        elif self.queue.get_length() == 1:
            return self.queue.head.val
        else:
            return self.queue.tail.val
        
    def empty(self) -> bool:
        return self.queue.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()