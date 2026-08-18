class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        openNode = []

        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    openNode.append((i, j))
                    board[i][j] = 'Z'

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    openNode.append((i, j))
                    board[i][j] = 'Z'

        q = openNode
        print(q)
        nq = []
        while q:
            for si, sj in q:
                # if board[si][sj] == 'O':
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nsi = si + di
                    nsj = sj + dj
                    if nsi >= 0 and nsi < m and nsj >= 0 and nsj < n and board[nsi][nsj] == 'O':
                        board[nsi][nsj] = 'Z'
                        nq.append((nsi, nsj))

            q, nq = nq, []

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'

