# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        same = True

        def dfs(p, q):
            nonlocal same
            if not same:
                return

            if not p and not q:
                return True

            if (not p and q) or (not q and p) or (q.val != p.val):
                same = False
                return

            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)

        return same