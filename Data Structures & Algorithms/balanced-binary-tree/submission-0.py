# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True

        def _dfs(root):
            if not self.balance:
                return 0

            if not root:
                return 0

            left = _dfs(root.left)
            right = _dfs(root.right)

            if abs(right-left) < 2:
                return max(left, right) + 1
            else:
                self.balance = False
                return 0

        _dfs(root)
        return self.balance

