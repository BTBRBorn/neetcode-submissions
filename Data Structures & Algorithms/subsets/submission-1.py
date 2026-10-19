class Solution:
    def decision_tree(self, index, nums, pset, subset):
        if index == len(nums):
            pset.append(subset.copy()) 
            return None
        
        subset.append(nums[index])
        self.decision_tree(index+1, nums, pset, subset)

        subset.pop()
        self.decision_tree(index+1, nums, pset, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        pset, subset = [], []
        self.decision_tree(0, nums, pset, subset)
        return pset
        