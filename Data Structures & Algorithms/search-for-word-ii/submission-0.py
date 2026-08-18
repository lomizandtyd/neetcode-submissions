class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self._ret = []
        self._trie_root = {'isWord': ''}
        self._build_trie(words)

        m, n = len(board), len(board[0])
        it = self._trie_root

        for i in range(m):
            for j in range(n):
                self._dfs(board, i, j, it)
        return list(set(self._ret))

    def _build_trie(self, words):
        for w in words:
            it = self._trie_root
            for c in w:
                if c not in it:
                    it[c] = {'isWord': ''}
                it = it[c]
            it['isWord'] = w

    def _dfs(self, board, m, n, it):
        if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]) or board[m][n] == '#' or board[m][n] not in it:
            return

        c = board[m][n]
        board[m][n] = '#'

        nit = it[c]

        if nit['isWord']:
            self._ret.append(nit['isWord'])
        self._dfs(board, m-1, n, nit)
        self._dfs(board, m+1, n, nit)
        self._dfs(board, m, n-1, nit)
        self._dfs(board, m, n+1, nit)
        board[m][n] = c


