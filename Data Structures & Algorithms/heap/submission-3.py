class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        
    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def percolate_down(self, i):
        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and
                self.heap[2*i+1] < self.heap[2*i] and
                self.heap[2*i+1] < self.heap[i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1
            elif self.heap[2*i] < self.heap[i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        self.percolate_down(i)
        return result


    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        nums.append(nums[0])
        nums[0] = 0
        self.heap = nums
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            self.percolate_down(cur)
            cur -= 1