# QuickSelect solution
class Solution:
    def middle(self, i, j, k, nums):
        arr = [(nums[i], i), (nums[j], j), (nums[k], k)]
        arr.sort(key=lambda x: x[0])
        return arr[1][1]

    def quickSelect(self, nums, s, e, k):
        #if e - s + 1 >= 3:
        #    m = (e + s) // 2
        #    p_index = self.middle(s, e, m, nums)
        #    nums[e], nums[p_index] = nums[p_index], nums[e]
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
            return nums[i]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums)-1, k)

        