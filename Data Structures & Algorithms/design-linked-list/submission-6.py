class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def getNode(self, index: int) -> ListNode | None:
        i = 0
        cur = self.head.next
        while i < index and cur:
            cur = cur.next
            i += 1
        if i == index:
            return cur
        return None

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node and node.next:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        next = self.head.next
        self.head.next = new_node
        next.prev = new_node
        new_node.prev = self.head
        new_node.next = next

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        prev = self.tail.prev
        self.tail.prev = new_node
        prev.next = new_node
        new_node.prev = prev
        new_node.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        next = self.getNode(index)
        if next is self.tail:
            self.addAtTail(val)
        else:
            prev = next.prev
            prev.next = new_node
            next.prev = new_node
            new_node.prev = prev
            new_node.next = next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.getNode(index)
        if cur and cur.next:
            prev = cur.prev
            next = cur.next
            prev.next, next.prev = next, prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)