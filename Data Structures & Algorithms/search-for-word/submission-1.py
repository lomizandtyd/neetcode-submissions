class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        m, n, l = len(board), len(board[0]), len(word)

        def dfs(cur, path, cid):
            x, y = cur
            if x >= 0 and y >= 0 and x < m and y < n:
                if board[x][y] == word[cid]:
                    if cid == l - 1:
                        return True

                    path.append((x, y))
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in path:
                            continue 
                        if dfs((nx, ny), path, cid+1):
                            return True
                    path.pop(-1)
            return False

        for i in range(m):
            for j in range(n):
                if dfs((i, j), [], 0):
                    return True

        return False