# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.l = []
        self.good = True

        def dfs(root):
            if not root or not self.good:
                return

            if root.left:
                dfs(root.left)

            if self.l and root.val <= self.l[-1].val:
                self.good = False
                return

            self.l.append(root)

            if root.right:
                dfs(root.right)

        dfs(root)
        return self.good