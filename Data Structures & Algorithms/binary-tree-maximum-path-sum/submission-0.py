# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(root):
            nonlocal maxSum 
            if not root:
                return 0

            lp = dfs(root.left)
            rp = dfs(root.right)

            np = root.val

            if lp >= 0:
                np += lp

            if rp >= 0:
                np += rp

            maxSum = max(maxSum, np)
            return max(root.val, root.val + lp, root.val + rp)

        dfs(root)

        return maxSum


            