class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indexes = []
        for i, e in enumerate(nums):
            if e == val:
                indexes.append(i)
        for i in reversed(indexes):
            nums.pop(i)
        return len(nums)