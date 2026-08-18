# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []

        def dfs(n):
            nonlocal ret
            if not n:
                ret.append("none")
                return

            ret.append(str(n.val))
            dfs(n.left)
            dfs(n.right)

        dfs(root)

        return ",".join(ret)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = []
        for v in data.split(','):
            if v == 'none':
                vals.append(None)
            else:
                vals.append(int(v))

        def dfs(i):
            nonlocal vals
            if i >= len(vals):
                return None, i

            if not vals[i]:
                return None, i+1

            root = TreeNode(vals[i])
            root.left, r = dfs(i+1)
            root.right, rr = dfs(r)
            return root, rr

        root, _ = dfs(0)
        return root
