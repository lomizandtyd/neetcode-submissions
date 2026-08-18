# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        pm_pre = {v: k for k, v in enumerate(preorder)}
        pm_in = {v: k for k, v in enumerate(inorder)}


        def _build(preS, preE, inS, inE):
            nonlocal preorder, inorder, pm_pre, pm_in
            if preS >= preE or preS >= len(preorder) or inS >= len(preorder):
                return None

            root_val = preorder[preS]
            in_l = (inS, pm_in[root_val])
            in_r = (in_l[1]+1, inE)

            pre_l = (preS+1, preS+1+in_l[1]-in_l[0])
            pre_r = (pre_l[1], preE)
            
            
            root = TreeNode(val=root_val)
            root.left = _build(pre_l[0], pre_l[1], in_l[0], in_l[1])
            root.right = _build(pre_r[0], pre_r[1], in_r[0], in_r[1])
            return root

        return _build(0, len(preorder), 0, len(inorder))
