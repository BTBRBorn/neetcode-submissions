class Solution:
    def reverseBits(self, n: int) -> int:
        def binaryRep(n):
            strbin = ""
            while n:
                strbin = str(n & 1) + strbin
                n = n >> 1
            return strbin
        strbin = binaryRep(n)[::-1]
        reverse = 0
        for i in range(len(strbin)):
            reverse += int(strbin[i]) * (2**(31-i))
        return reverse


        

        