class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] < target:
                low = middle + 1 
            elif nums[middle] > target:
                high = middle - 1
            else:
                return middle
        
        return -1

        