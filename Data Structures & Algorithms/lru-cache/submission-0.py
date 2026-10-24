class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key to ListNode
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def append(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev, node.next = prev, self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        newNode = ListNode(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = newNode
        self.append(self.cache[key])
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
