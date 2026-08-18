class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        table = [i for i in range(n)]

        def find(k):
            nonlocal table
            if k != table[k]:
                table[k] = find(table[k])
                return table[k]
            else:
                return k

        def union(i, j):
            nonlocal table
            k = find(i)
            v = find(j)
            
            if k < v:
                table[v] = k
            else:
                table[k] = v


        for i, j in edges:
            union(i, j)

        for i in range(n):
            find(i)

        return len(set(table))