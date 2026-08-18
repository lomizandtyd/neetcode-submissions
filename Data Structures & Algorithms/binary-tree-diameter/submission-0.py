# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def _dfs(root):
            
            if not root:
                return 0, 0

            l_depth, l_diameter = _dfs(root.left)
            r_depth, r_diameter = _dfs(root.right)

            depth = max(l_depth, r_depth) + 1
            diameter = max(l_diameter, r_diameter, l_depth+r_depth)

            return depth, diameter

        return _dfs(root)[1]