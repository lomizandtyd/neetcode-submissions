class Solution:
    def climbStairs(self, n: int) -> int:
        p0 = 1
        p1 = 1

        if n <= 1:
            return 1

        for i in range(2, n+1):
            pi = p0 + p1
            p0, p1 = p1, pi

        return pi