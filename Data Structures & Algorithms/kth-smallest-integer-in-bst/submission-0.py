# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []

        def dfs(root):
            nonlocal k
            if not root or len(self.l) >= k:
                return
            dfs(root.left)
            self.l.append(root.val)
            dfs(root.right)

        dfs(root)

        return self.l[k-1]

