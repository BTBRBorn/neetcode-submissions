class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        bits = [0, 1]
        while len(bits) < n + 1:
            for i in range(len(bits)):
                bits.append(1 + bits[i])
                if len(bits) == n + 1:
                    break
        return bits