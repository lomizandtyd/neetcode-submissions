"""
   c r a b t
a  0 0 1 1 1
c  1 1 1 1 1 
a  1 1 2 2 2
t  1 1 2 2 3
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        if m == 0 or n == 0:
            return 0

        dp = [[0] * (n+1) for i in range(m+1)]

        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = max(dp[i-1][0], 1 if text1[i]==text2[0] else 0)

        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], 1 if text1[0] == text2[i] else 0)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(
                    dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1] + (1 if text1[i] == text2[j] else 0)
                )

        return dp[m-1][n-1]
        