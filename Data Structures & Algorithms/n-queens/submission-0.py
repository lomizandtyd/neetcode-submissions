class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        stat = [['.'] * n for i in range(n)]

        res = []
        def dfs(i, stat):
            # print("\n", i)
            # print(stat)
            for j in range(n):
                if stat[i][j] != '.':
                    continue

                nstat = [r.copy() for r in stat]
                nstat[i][j] = 'Q'
                if i == n-1:
                    for i in range(n):
                        for j in range(n):
                            if nstat[i][j] == 'X':
                                nstat[i][j] = '.'
                    res.append([''.join(r) for r in nstat])
                    continue

                for k in range(n):
                    if nstat[i][k] != 'Q':
                        nstat[i][k] = 'X'

                dis = 1
                for k in range(i+1, n):
                    nstat[k][j] = 'X'

                    if j + dis < n:
                        nstat[k][j+dis] = 'X'
                    if j - dis >= 0:
                        nstat[k][j-dis] = 'X'
                    dis += 1
                dfs(i+1, nstat)

        dfs(0, stat)

        return res


