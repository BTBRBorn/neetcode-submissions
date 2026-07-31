class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indexes = []
        for i, e in enumerate(nums):
            if e == val:
                indexes.append(i)
        for i in range(len(indexes)-1, -1, -1):
            nums.pop(indexes[i])
        return len(nums)