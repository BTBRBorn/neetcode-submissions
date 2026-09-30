import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(piles, k):
            return sum([math.ceil(p/k) for p in piles])
        low, high = 1, max(piles)
        middle = (low + high) // 2
        while high >= low:
            if time(piles, middle) > h:
                low = middle + 1
            elif time(piles, middle) <= h:
                k = middle
                high = middle - 1
            middle = (low + high) // 2
            
        return k 