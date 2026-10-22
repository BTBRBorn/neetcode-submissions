class MaxHeap:
    def __init__(self):
        self.heap = [0]
    
    def percolate_down(self, i):
        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and
                self.heap[2*i+1] > self.heap[2*i] and
                self.heap[2*i+1] > self.heap[i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1
            elif self.heap[2*i] > self.heap[i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            else:
                break
    
    def heapify(self, arr):
        if not arr:
            return None
        arr.append(arr[0])
        arr[0] = 0
        self.heap = arr
        curr = (len(self.heap) - 1) // 2
        while curr > 0:
            self.percolate_down(curr)
            curr -= 1
    
    def pop(self):
        if len(self.heap) == 1:
            raise ValueError("Heap is empty.")
        if len(self.heap) == 2:
            return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return result

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap()
        heap.heapify(nums)
        for _ in range(k):
            kth = heap.pop()
        return kth
        