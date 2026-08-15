class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        try:
            return self.memo[n]
        except:
            if n == 0:
                return 1
            elif n < 0:
                return 0
            count = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n] = count
            return count

        