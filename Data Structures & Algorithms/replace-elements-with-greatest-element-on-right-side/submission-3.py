class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            cur_val = arr[i]
            arr[i] = max_val
            if cur_val > max_val:
                max_val = cur_val
        return arr