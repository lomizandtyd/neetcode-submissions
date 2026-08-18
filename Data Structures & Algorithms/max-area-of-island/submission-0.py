class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxa = 0

        def _dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1
            area += _dfs(grid, i-1, j)
            area += _dfs(grid, i+1, j)
            area += _dfs(grid, i, j+1)
            area += _dfs(grid, i, j -1)
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxa = max(maxa, _dfs(grid, i, j))
        return maxa
