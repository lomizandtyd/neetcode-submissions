class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def _dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            _dfs(grid, i-1, j)
            _dfs(grid, i+1, j)
            _dfs(grid, i, j+1)
            _dfs(grid, i, j -1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                _dfs(grid, i, j)

        return cnt
            