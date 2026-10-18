# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def tree_sum(node, s):
            if not node:
                return False
            s += node.val
            if not node.left and not node.right:
                return s == targetSum
            if tree_sum(node.left, s):
                return True
            if tree_sum(node.right, s):
                return True
            return False
        return tree_sum(root, 0)

        
        