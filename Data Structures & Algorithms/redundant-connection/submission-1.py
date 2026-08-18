class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        fa = [i for i in range(n)]

        def find(i):
            nonlocal fa
            if i == fa[i]:
                return i
            fa[i] = find(fa[i])
            return fa[i]

        def union(i, j):
            nonlocal fa
            k, v = find(i), find(j)

            if k < v:
                fa[v] = k
            elif k > v:
                fa[k] = v
            else:
                return False

            return True

        for i, j in edges:
            if not union(i-1, j-1):
                return [i, j]

        return []
