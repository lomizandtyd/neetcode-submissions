class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 1. collect all treasure chest, push to list (i, j, dis=0)
        # 2. bfs start from chest point, stop until meet -1, 0, or boundary, update dist by min(dis_old, dis_new)

        m, n = len(grid), len(grid[0])

        chests = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    chests.append((i, j, 0))

        visited = set()
        q = chests# [(i, j, 0)]
        nq = []
        while q:
            for si, sj, dis in q:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nsi = si + dx
                    nsj = sj + dy
                    if nsi >= 0 and nsi < m and nsj >=0 and nsj < n and (nsi, nsj) not in visited and grid[nsi][nsj] > 0:
                        visited.add((nsi, nsj))
                        grid[nsi][nsj] = min(grid[nsi][nsj], dis+1)
                        nq.append((nsi, nsj, grid[nsi][nsj]))

            q, nq = nq, []


