class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(n):
            count = 0
            while n > 0:
                count += n & 1
                n = n >> 1
            return count
        return [countBits(i) for i in range(n+1)]
        