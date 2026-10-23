# QuickSelect solution
class Solution:
    def quickSelect(self, nums, s, e, k):
        pivot, i = nums[e], s
        for j in range(s, e):
            if pivot > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[e] = nums[e], nums[i]
        if k > i:
            return self.quickSelect(nums, i+1, e, k)
        elif k < i:
            return self.quickSelect(nums, s, i-1, k)
        else:
            return nums[k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums)-1, k)

        