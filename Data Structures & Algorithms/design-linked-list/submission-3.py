class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        i = 0
        while i != index and id(cur) != id(self.right):
            cur = cur.next
            i += 1

        if id(cur) != id(self.right):
            return cur.val
        else:
            return -1
    
    def get_node(self, index: int):
        cur = self.left.next
        i = 0
        while i != index and cur:
            cur = cur.next
            i += 1
        return cur

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        next = self.left.next
        self.left.next = new_head
        next.prev = new_head
        new_head.prev = self.left
        new_head.next = next

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        prev = self.right.prev
        prev.next = new_tail
        self.right.prev = new_tail
        new_tail.next = self.right
        new_tail.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        next_node = self.get_node(index)
        if next_node:
            prev_node = next_node.prev
            prev_node.next = new_node
            next_node.prev = new_node
            new_node.next = next_node
            new_node.prev = prev_node

    def deleteAtIndex(self, index: int) -> None:
        cur_node = self.get_node(index)
        if cur_node and id(cur_node) != id(self.right):
            prev_node = cur_node.prev
            next_node = cur_node.next
            prev_node.next = next_node
            next_node.prev = prev_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)