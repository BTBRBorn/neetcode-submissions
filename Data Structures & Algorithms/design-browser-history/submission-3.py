class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.homepage
        self.tail.prev = self.homepage
        self.homepage.prev = self.head
        self.homepage.next = self.tail
        self.current = self.homepage

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.current.next = new_node
        self.tail.prev = new_node
        new_node.prev = self.current
        new_node.next = self.tail
        self.current = new_node

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.prev is not self.head:
            self.current = self.current.prev 
            i += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.next is not self.tail:
            self.current = self.current.next
            i +=1
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)