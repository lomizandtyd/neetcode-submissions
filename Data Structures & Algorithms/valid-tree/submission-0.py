class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        visited = set()
        graph = [list() for i in range(n)]

        for ei, ej in edges:
            graph[ei].append(ej)
            graph[ej].append(ei)
        
        def dfs(i, p):
            nonlocal graph
            if i in visited:
                return False

            visited.add(i)
            for j in graph[i]:
                if j == p:
                    continue

                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n