class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        cur_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if cur_count > max_count:
                    max_count = cur_count
                cur_count = 0
            elif nums[i] == 1:
                cur_count += 1
        if cur_count > max_count:
            max_count = cur_count
        return max_count
