# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count):
            if not node:
                return count, None
            count, val = dfs(node.left, count)
            count += 1
            if count == k:
                val = node.val
            if val is not None: return count, val
            count, val = dfs(node.right, count)
            return count, val
        return dfs(root, 0)[1]
