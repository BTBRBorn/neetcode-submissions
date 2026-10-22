import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x < y:
                new_weight = y - x
                heapq.heappush_max(stones, new_weight)
        if stones:
            return stones[0]
        else:
            return 0
        