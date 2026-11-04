class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            cache[0], cache[1] = cache[1], max(cache[0] + nums[i], cache[1])
        return cache[1]

