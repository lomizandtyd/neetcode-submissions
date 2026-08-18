# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p_path = []
        self.q_path = []

        self.stack = []

        def dfs(node):
            if not node:
                return

            if self.p_path and self.q_path:
                return

            self.stack.append(node)

            if node == p:
                self.p_path = list(self.stack)

            if node == q:
                self.q_path = list(self.stack)

            dfs(node.left)
            dfs(node.right)

            self.stack.pop(-1)

        dfs(root)

        pidx = 0
        while pidx < len(self.p_path) and pidx < len(self.q_path) and self.p_path[pidx] == self.q_path[pidx]:
            pidx += 1

        return self.p_path[pidx-1]

