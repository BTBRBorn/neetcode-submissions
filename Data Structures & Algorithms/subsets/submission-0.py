class Solution:
    def strBinary(self, n, buffer_size):
        strbin = ''
        while n > 0:
            r = n % 2
            n //= 2
            strbin = str(r) + strbin 
        if buffer_size > len(strbin):
            strbin = '0'*(buffer_size - len(strbin)) + strbin
        return strbin

        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pset = []
        for i in range(2**len(nums)):
            strbin = self.strBinary(i, len(nums))
            subset = []
            for j, b in enumerate(strbin):
                if b == '1':
                    subset.append(nums[j])
            pset.append(subset)
        return pset
        