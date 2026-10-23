class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            if (target - n) in h:
                j = h[target-n]
                if i != j:
                    return [i, j] 
