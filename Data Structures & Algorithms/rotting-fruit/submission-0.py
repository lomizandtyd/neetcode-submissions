class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        # bfs broadcast
        q = rotten
        nq = []
        ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0

        while q:
            for si, sj in q:
                for dx, dy in ds:
                    nsi = si + dx
                    nsj = sj + dy

                    if nsi >= 0 and nsi < m and nsj >=0 and nsj < n and grid[nsi][nsj] == 1:
                        grid[nsi][nsj] = 2
                        nq.append((nsi, nsj))

            q, nq = nq, []
            if len(q) > 0:
                minutes += 1
    
        # check remains
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minutes