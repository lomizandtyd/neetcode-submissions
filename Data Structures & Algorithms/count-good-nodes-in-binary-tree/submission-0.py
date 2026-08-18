# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = []

        def dfs(root, maxi=-999):
            if not root:
                return

            if root.val >= maxi:
                self.good.append(root)
                maxi = root.val

            dfs(root.left, maxi)
            dfs(root.right, maxi)

        dfs(root)

        return len(self.good)