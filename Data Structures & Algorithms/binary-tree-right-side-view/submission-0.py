# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.view = []

        def bfs(n):
            if not n:
                return
 
            s = [n]
            s2 = []

            while len(s) > 0:
                for nn in s:
                    if nn.left:
                        s2.append(nn.left)
                    if nn.right:
                        s2.append(nn.right)
                self.view.append(s[-1].val)
                s, s2 = s2, []

        bfs(root)
        return self.view

            