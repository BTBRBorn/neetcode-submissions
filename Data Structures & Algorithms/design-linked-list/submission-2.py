class ListNode:
    def __init__(self, val=0):
        self.prev = None
        self.next = None
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while node and i != index:
            node = node.next 
            i += 1
        if node is None:
            return -1
        return node.val

    def getNode(self, index: int) -> int:
        node = self.head
        i = 0
        while node and i != index:
            node = node.next 
            i += 1
        if node is None:
            return -1
        return node

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            new_node = ListNode(val)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = ListNode(val)
            self.head = self.tail
        else:
            new_node = ListNode(val)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            return 
        else:
            front = self.getNode(index)
            back = front.prev
            new_node = ListNode(val)
            back.next = new_node
            front.prev = new_node
            new_node.prev = back
            new_node.next = front
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node == -1:
            return
        else:
            back = node.prev
            front = node.next
            if back is None:
                self.head = self.head.next
                self.head.prev = None
            elif front is None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                back.next = front
                front.prev = back
        self.length -= 1
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)