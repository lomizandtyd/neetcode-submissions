class Solution:
    def reverse(self, x: int) -> int:
        y = 0

        neg = 1
        if x < 0:
            x = -x
            neg = -1

        while x:
            y = y * 10 + x % 10
            x = x // 10

        if y >= 0x7fffffff-1:
            return 0

        return neg * y