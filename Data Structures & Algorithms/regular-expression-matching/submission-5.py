class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if i == m and j == n:
                return True

            if (i,j) in cache:
                return cache[(i,j)]


            match = False

            # match cases:
            # 1. s[i] == p[j] != '.'
            # 2. p[j] = '.'
            #

            if j < n and i < m and (p[j] == '.' or s[i] == p[j]):
                # matched
                # if p[j+1] != '*', continue
                if j+1 <n:
                    if p[j+1] != '*':
                        match = dfs(i+1, j+1)
                    else:
                        match = dfs(i+1, j) or dfs(i+1, j+2) or dfs(i, j+2)
                else:
                    match = (i+1) == m
            else:
                if j+1 < n and p[j+1] == '*':
                    match = dfs(i, j+2)

            # print(s[i:], p[j:], match)
            cache[(i,j)] = match
            return match

        return dfs(0, 0)

            