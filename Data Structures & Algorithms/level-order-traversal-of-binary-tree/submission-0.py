# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def bfs(root):
            nonlocal ret
            stack = [root]
            s2 = []

            while len(stack) > 0:
                for n in stack:
                    if n.left:
                        s2.append(n.left)
                    if n.right:
                        s2.append(n.right)

                ret.append([n.val for n in stack if n])
                stack, s2 = s2, []

        if not root:
            return []

        bfs(root)
        return ret

                
                