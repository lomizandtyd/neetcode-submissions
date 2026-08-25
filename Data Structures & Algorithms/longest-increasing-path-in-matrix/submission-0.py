class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        if m == 0 or n == 0:
            return 0

        p = [[-1] * n for _ in range(m)]


        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return -1e9

            if p[i][j] > 0:
                return p[i][j]

            res = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, dfs(ni, nj)+1)

            p[i][j] = res
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        # print(p)
        return res

