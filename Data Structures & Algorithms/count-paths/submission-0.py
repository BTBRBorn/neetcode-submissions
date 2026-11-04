class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1]*n
        for _ in range(m-1):
            nextRow = [0] * n
            nextRow[-1] = 1
            for i in range(n-2, -1, -1):
                nextRow[i] = prevRow[i] + nextRow[i+1]
            prevRow = nextRow

        return prevRow[0]
        