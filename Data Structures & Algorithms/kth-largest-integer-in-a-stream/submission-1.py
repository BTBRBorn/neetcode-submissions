class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for val in nums:
            self.push(val)
        while len(self.heap) > k + 1:
            self.pop()

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1 
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) == self.k + 2:
            self.pop()
        return self.heap[1]
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and
                self.heap[2*i+1] < self.heap[2*i] and
                self.heap[2*i+1] < self.heap[i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1
            elif self.heap[2*i] < self.heap[i]: 
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break
        return result
        
