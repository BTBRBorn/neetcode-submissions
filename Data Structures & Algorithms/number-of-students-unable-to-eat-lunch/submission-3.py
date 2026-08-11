class ListNode:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val: int) -> None:
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
            val = None
        elif self.get_length() == 1:
            val = self.head.val
            self.head = None
            self.length -= 1
        elif self.get_length() == 2:
            val = self.head.val
            self.head = self.tail
            self.tail = None
            self.length -= 1
        else:
            val = self.head.val
            self.head = self.head.next
            self.length -= 1
        return val

    def head_to_tail(self):
        if self.get_length() > 1:
            val = self.dequeue()
            self.enqueue(val)
    
    def isEmpty(self):
        return self.get_length() == 0

    def get_length(self):
        return self.length

    def from_list(self, data: List[int]):
        if data:
            for val in data:
                self.enqueue(val)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsQ = Queue()
        sandwichQ = Queue()
        studentsQ.from_list(students)
        sandwichQ.from_list(sandwiches)
        counter = 0
        while not studentsQ.isEmpty() and not sandwichQ.isEmpty():
            if studentsQ.head.val == sandwichQ.head.val:
                studentsQ.dequeue()
                sandwichQ.dequeue()
                counter = 0
            else:
                studentsQ.head_to_tail()
                counter +=1
            if counter == studentsQ.get_length():
                break
        return studentsQ.get_length()





        