class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(31, -1, -1):
            b = n & 1    
            reverse += b * 2**i 
            n = n >> 1
            if n == 0:
                break
        return reverse

        