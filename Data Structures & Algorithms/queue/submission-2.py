class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def isEmpty(self) -> bool:
        return self.head.next is self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        prev = self.tail.prev
        prev.next = new_node
        self.tail.prev = new_node
        new_node.prev = prev
        new_node.next = self.tail

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        next = self.head.next
        self.head.next = new_node
        next.prev = new_node
        new_node.prev = self.head
        new_node.next = next

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next
        return node.val